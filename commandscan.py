#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
from mysql import connector
from lib import log
from lib import command
from config import mysql as mysql_con


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
                        CommandScan.trans(row[0], row[1])

                    cursor.close()

                    time.sleep(1)

                except Exception as e:
                    log.exp("扫描音频文件发生异常: ", e)

                finally:
                    if "" != conn:
                        conn.close()

        except Exception as e:
            log.exp("扫描数据库未完成命令", e)

    # 翻译命令
    @staticmethod
    def trans(command_id, content):
        try:
            log.normal("执行命令： 命令编号: %d 内容: %s" % (command_id, content))

            try:
                conn = ""
                conn = connector.connect(host=mysql_con.HOST,
                                         user=mysql_con.USERNAME,
                                         password=mysql_con.PASSWORD,
                                         port=mysql_con.PORT,
                                         database=mysql_con.DATABASE,
                                         charset=mysql_con.CHARSET)
                cursor = conn.cursor()
                cursor.execute("""SELECT * FROM translates WHERE
                                (`type`=1 AND command=%s)
                                OR
                                (`type`=0 AND command LIKE %s)""",
                               (content, "%" + content + "%", ))

                is_exec = False
                # 获取所有记录
                row = cursor.fetchone()
                if None is not row:
                    # 处理
                    CommandScan.deal(row[0], row[2], row[3])
                    is_exec = True

                cursor.close()
                if False is is_exec:
                    log.normal("命令未执行： 命令编号: %d 内容: %s" % (command_id, content))

            except Exception as e:
                log.exp("翻译命令: %s" % content, e)

            finally:
                command.Command.exec(command_id)
                if "" != conn:
                    conn.close()

        except Exception as e:
            log.exp("翻译命令： 命令编号: %d 内容: %s" % (command_id, content), e)

    # 处理命令
    @staticmethod
    def deal(trans_id, trans_script_name,trans_script_arvg):
        try:
            log.normal("执行命令： 命令编号: %d 脚本名称: %s 参数：%s" % (trans_id, trans_script_name, trans_script_arvg))

            os.system("python script/%s %s" % (trans_script_name, trans_script_arvg))

        except Exception as e:
            log.exp("执行命令： 命令编号: %d 脚本名称: %s 参数：%s" % (trans_id, trans_script_name, trans_script_arvg), e)
