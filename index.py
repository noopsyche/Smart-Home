#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
from voicesan import VoiceScan
from commandscan import CommandScan
import recode


# 子进程创建
def sub_process(name):

    if "start_recode" == name:
        recode.start()

    if "start_voice_scan" == name:
        VoiceScan.start()

    if "start_command_scan" == name:
        CommandScan.start()


# 运行主函数
def main():
    # 监听音频
    Process(target=sub_process, args=('start_recode',)).start()

    # 扫描音频文件
    Process(target=sub_process, args=('start_voice_scan',)).start()

    # 扫描未处理命令
    Process(target=sub_process, args=('start_command_scan',)).start()

if __name__ == '__main__':
    main()
