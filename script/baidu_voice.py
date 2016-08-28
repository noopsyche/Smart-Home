#!/usr/bin/python
# -*- coding: utf-8 -*-
import config.recode as config
from urllib import request, parse
import pycurl
import wave
import json
import os
import time
import random
from datetime import datetime
from pygame import mixer
from script import command
from script import log


class Voice:
    # 缓存的access_token
    access_token_cache = ""

    # 获取access_token
    # 参照地址：http://yuyin.baidu.com/docs/tts/135#获取 Access Token
    @staticmethod
    def get_access_token():
        if "" != Voice.access_token_cache:
            log.normal("从缓存获取baidu_access_token成功")
            return Voice.access_token_cache
        # access_token 保存文件
        access_token_filename = "cache/token/baidu_access_token"
        # 计算时间差，21天换一次
        modifiedtime = time.localtime(os.stat(access_token_filename).st_mtime)
        y = time.strftime('%Y', modifiedtime)
        m = time.strftime('%m', modifiedtime)
        d = time.strftime('%d', modifiedtime)

        try:
            if 21 > (datetime.now() - datetime(int(y), int(m), int(d))).days:
                with open(access_token_filename, "r") as file:
                    Voice.access_token_cache = file.read()
                    log.normal("从文件获取baidu_access_token成功")
                    return Voice.access_token_cache

        except BaseException as e:
                log.exp("获取baidu_access_token发生异常。", e)
                return False

        # 请求地址
        grant_type = "client_credentials"       # 固定值
        client_id = "dnHpAdOFm2jxG0rmnfDbxSsT"  # api key
        client_secret = "c5046dee23e31cf9b542953425f7821e"  # secret key
        request_url_token = "https://openapi.baidu.com/oauth/2.0/token?grant_type=" + grant_type\
                            + "&client_id=" + client_id \
                            + "&client_secret=" + client_secret

        try:
            with request.urlopen(request_url_token) as f:
                data = f.read()
                if 200 != f.status:
                    # 获取错误，返回false
                    log.warning("获取baidu_access_token失败，网络错误")
                    return False
                data = json.loads(data.decode('utf-8'))
                log.normal("获取baidu_access_token成功")

                # 保存到文件
                with open(access_token_filename, "w") as file:
                    file.write(data["access_token"])

                Voice.access_token_cache = data["access_token"]

                return Voice.access_token_cache

        except Exception as e:
                log.exp("获取baidu_access_token发生异常。", e)
                return False

    # 输出语音信息
    @staticmethod
    def parse_text_result(data):
        data = json.loads(data.decode("utf-8"))
        if "success." == data["err_msg"]:
            result = data["result"][0]
            command.Command.insert(result)

        else:
            log.warning("语音转文字失败。原因：" + data["err_msg"])

    '''
        通过语音文件内容获取文本信息
        @param file_name 语音文件地址，wav格式
    '''
    @classmethod
    def get_text(cls, file_name):
        log.normal("音频转文字: " + file_name)
        # 请求地址
        request_url = "http://vop.baidu.com/server_api"

        # 参数
        p_rate = config.RATE  # 采样率，支持 8000 或者 16000
        p_cuid = "FC-AA-14-D0-1D-67"  # 用户唯一标识，用来区分用户，填写机器 MAC 地址，长度为60以内
        p_token = cls.get_access_token()  # 开放平台获取到的开发者 access_token
        fp = wave.open(file_name, 'rb')
        nf = fp.getnframes()
        p_len = nf * 2
        p_speech = fp.readframes(nf)

        srv_url = request_url + '?cuid=' + p_cuid + '&token=' + p_token
        http_header = [
            'Content-Type: audio/pcm; rate=%d' % p_rate,
            'Content-Length: %d' % p_len
        ]

        c = pycurl.Curl()
        c.setopt(pycurl.URL, str(srv_url))   # curl doesn't support unicode
        c.setopt(c.HTTPHEADER, http_header)  # must be list, not dict
        c.setopt(c.POST, 1)
        c.setopt(c.CONNECTTIMEOUT, 30)
        c.setopt(c.TIMEOUT, 30)
        c.setopt(c.WRITEFUNCTION, cls.parse_text_result)
        c.setopt(c.POSTFIELDS, p_speech)
        c.setopt(c.POSTFIELDSIZE, p_len)
        try:
            c.perform()
        except Exception as e:
            log.exp("语音转文字发生异常。", e)

    '''
        文字信息转音频
        @param text 欲转换成音频的文字
    '''
    @classmethod
    def tts(cls, text):
        if len(text) > 1024:
            log.warning("tts文本过长")
            return False

        log.normal("TTS: " + text)
        # 参数
        p_token = cls.get_access_token()  # 开放平台获取到的开发者 access_token
        p_cuid = "FC-AA-14-D0-1D-67"  # 用户唯一标识，用来区分用户，填写机器 MAC 地址，长度为60以内
        request_url = "http://tsn.baidu.com/text2audio?"
        data = {
            "tex": text,
            "lan": "zh",
            "tok": p_token,
            "cuid": p_cuid,
            "ctp": 1,
            "spd": "4",
            "pit": "4",
            "vol": "9",
            "per": "3",
        }
        request_url_tts = request_url + parse.urlencode(data)

        try:
            with request.urlopen(request_url_tts) as f:
                data = f.read()
                if 200 != f.status:
                    # 获取错误，返回false
                    log.warning("获取baidu_tts失败，网络错误")
                    return False
                log.normal("获取baidu_tts成功")

                # 保存到文件
                random.seed()
                filename = "cache/mp3/" + datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + \
                           str(random.randint(0, 99999)) + ".mp3"

                with open(filename, "wb") as file:
                    file.write(data)

                # 播放
                cls.play_mp3(filename)
                return True

        except Exception as e:
                log.exp("获取baidu_tts发生异常。", e)
                return False

    '''
        播放mp3文件
    '''
    @staticmethod
    def play_mp3(filename):
        log.normal("播放MP3 " + filename)
        try:
            freq = 16000  # 16kbs
            mixer.init(freq)
            if os.path.isfile(filename):
                if os.path.getsize(filename):
                    mixer.music.load(filename)
                    mixer.music.play()
                else:
                    log.warning("播放MP3错误,文件不存在：" + filename)
            else:
                log.warning("播放MP3错误,文件不存在：" + filename)
        except Exception as e:
            log.exp("播放MP3发生异常。", e)
