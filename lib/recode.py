#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyaudio
import numpy as np
from datetime import datetime
import wave
import config.recode as config
from lib import log

# 将data中的数据保存到名为filename的WAV文件中


def save_wave_file(file_name, data):
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(config.RATE)
    wf.writeframes(b''.join(data))
    wf.close()


# 开始录音


def start():
    # 开启声音输入
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=config.RATE, input=True,
                     frames_per_buffer=config.NUM_BLOCK)

    save_count = 0
    save_buffer = []
    start_recode = 0
    log.normal("recode listen start...")
    while True:
        # 读入NUM_SAMPLES个取样
        string_audio_data = stream.read(config.NUM_BLOCK)
        # 将读入的数据转换为数组
        audio_data = np.fromstring(string_audio_data, dtype=np.short)
        # 计算大于LEVEL的取样的个数
        large_sample_count = np.sum(audio_data > config.LEVEL)
        if large_sample_count < config.COUNT_NUM:
            # 未达到记录等级
            if save_count > 1:
                save_count -= 1
                save_buffer.append(string_audio_data)
            else:
                if 1 == start_recode:
                    start_recode = 0
                    save_buffer.append(string_audio_data)
                    log.normal("recode over")
                else:
                    save_buffer = [string_audio_data, ]
        else:
            # 达到记录等级
            # 将要保存的数据存放到save_buffer中
            save_buffer.append(string_audio_data)
            if 0 == start_recode:
                save_count = config.SAVE_LENGTH
                start_recode = 1
                log.normal("recode start")

        if 0 == start_recode:
            # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
            if len(save_buffer) > 1:
                filename = "cache/sound/before_" + datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
                save_wave_file(filename, save_buffer)
                save_buffer = []
                log.normal(filename + " saved")
