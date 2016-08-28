#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from mysql import connector
from script import log
from script import command
from config import mysql as mysql_con
from script import baidu_voice
from script import serial


class CommandScan:

    # 扫描数据库中未完成的命令
    @staticmethod
    def start():
        # 扫描目录
        log.normal("开始扫描数据库中未完成的命令...")
        try:
            conn = ""
            while True:
                try:
                    conn = connector.connect(host=mysql_con.HOST,
                                             user=mysql_con.USERNAME,
                                             password=mysql_con.PASSWORD,
                                             port=mysql_con.PORT,
                                             database=mysql_con.DATABASE,
                                             charset=mysql_con.CHARSET)
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM command WHERE status=%s ORDER BY posttime",
                                   ('0', ))

                    # 获取所有记录
                    results = cursor.fetchall()
                    for row in results:
                        # 处理
                        CommandScan.deal(row[0], row[1])

                    cursor.close()

                    time.sleep(1)

                except Exception as e:
                    log.exp("扫描音频文件发生异常: ", e)

                finally:
                    if "" != conn:
                        conn.close()

        except Exception as e:
            log.exp("扫描数据库未完成命令", e)

    # 处理命令
    @staticmethod
    def deal(command_id, content):
        try:
            log.normal("执行命令： 命令编号: %d 内容: %s" % (command_id, content))

            if -1 != content.find("开"):
                log.debug("开灯")
                serial.Serial.open_light()

            if -1 != content.find("关 vc"):
                log.debug("关灯")
                serial.Serial.close_light()

            command.Command.exec(command_id)
            baidu_voice.Voice.tts("执行完毕")

        except Exception as e:
            log.exp("执行命令： 命令编号: %d 内容: %s" % (command_id, content), e)