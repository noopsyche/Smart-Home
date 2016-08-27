#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
from voicesan import VoiceScan
import recode


# 子进程创建
def sub_process(name):

    if "start_recode" == name:
        recode.start()

    if "start_voice_scan" == name:
        VoiceScan.start()


# 运行主函数
def main():
    # 监听音频
    Process(target=sub_process, args=('start_recode',)).start()

    # 扫描音频文件
    Process(target=sub_process, args=('start_voice_scan',)).start()

if __name__ == '__main__':
    main()
