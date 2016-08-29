#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from lib import log
from lib import baidu_voice


class VoiceScan:

    # 扫描音频文件
    @staticmethod
    def start():
        # 扫描目录
        root_dir = "cache/sound"
        log.normal("开始扫描音频文件...")
        while True:
            try:
                for file in os.listdir(root_dir):
                    # 搜索 before_ 开头的wav文件
                    re_wav = re.compile(r'^before_(.+)')
                    m = re_wav.match(file)
                    if m:
                        # 开始处理音频文件
                        VoiceScan.deal(m.group(1))

            except Exception as e:
                log.exp("扫描音频文件发生异常: ", e)

    # 处理音频文件
    @staticmethod
    def deal(filename):
        try:
            filename_before = "cache/sound/" + "before_" + filename
            log.normal("开始处理音频文件：" + filename_before)
            # 转换文字
            baidu_voice.Voice.get_text(filename_before)

            # 重命名文件，避免表明重复扫描
            os.rename(filename_before, "cache/sound/" + "end_" + filename)
            log.normal("音频文件处理完毕：" + filename_before)

        except Exception as e:
            log.exp("处理音频文件发生异常: ", e)
