#!/usr/bin/python
# -*- coding: utf-8 -*-
# 串口操作脚本

import sys
import re
from lib import serial
from lib import baidu_voice


def process(content):
    serial.Serial.write_hex("COM6", content)
    baidu_voice.Voice.tts("执行完毕")


if __name__ == '__main__':
    p = re.compile("-")
    param = p.sub(" ", sys.argv[1])
    process(param)

