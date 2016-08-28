#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from mysql import connector
from script import log
from config import mysql as mysql_con


class Command:

    # 往数据库里插入一条命令
    @staticmethod
    def insert(text):
        try:
            conn = ""
            conn = connector.connect(host=mysql_con.HOST,
                                     user=mysql_con.USERNAME,
                                     password=mysql_con.PASSWORD,
                                     port=mysql_con.PORT,
                                     database=mysql_con.DATABASE,
                                     charset=mysql_con.CHARSET)

            cursor = conn.cursor()
            cursor.execute("INSERT INTO command (`content`,`status`,`posttime`) VALUES (%s,%s,%s)",
                           (text, 0, datetime.timestamp(datetime.now())))

            # 提交记录
            conn.commit()

            log.normal("往数据库中插入新命令：" + text)

        except Exception as e:
            log.exp("往数据库中插入新命令：" + text, e)

        finally:
            if "" != conn:
                conn.close()

    # 执行完毕后设置命令状态为已完成
    @staticmethod
    def exec(command_id):
        try:
            conn = ""
            conn = connector.connect(host=mysql_con.HOST,
                                     user=mysql_con.USERNAME,
                                     password=mysql_con.PASSWORD,
                                     port=mysql_con.PORT,
                                     database=mysql_con.DATABASE,
                                     charset=mysql_con.CHARSET)

            cursor = conn.cursor()
            cursor.execute("UPDATE  command  SET `status`=%s WHERE id=%s",
                           ('1', command_id))

            # 提交记录
            conn.commit()

            log.normal("更新命令状态 命令编号：%d" % command_id)

        except Exception as e:
            log.exp("更新命令状态 命令编号：%d" % command_id, e)

        finally:
            if "" != conn:
                conn.close()