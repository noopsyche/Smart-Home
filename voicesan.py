#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from lib import log
import re


class VoiceScan:
    # 扫描音频文件
    def start(self):
        # 扫描目录
        root_dir = "cache/sound"
        log.debug("开始扫描音频文件...")
        while True:
            try:
                for file in os.listdir(root_dir):
                    # 搜索 before_ 开头的wav文件
                    re_wav = re.compile(r'^before_(.+)')
                    m = re_wav.match(file)
                    if m:
                        # 开始处理音频文件
                        self.deal(m.group(1))

            except OSError as e:
                log.error("扫描音频文件发生系统错误: " + e)

    # 处理音频文件
    @staticmethod
    def deal(filename):
        try:
            log.normal("开始处理音频文件：" + filename)
            filename = "before_" + filename

            log.normal("音频文件处理完毕：" + filename)

        except OSError as e:
            log.error("处理音频文件发生系统错误: " + e)
