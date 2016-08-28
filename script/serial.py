#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import binascii


class Serial:

    # 开灯
    @staticmethod
    def open_light():
        conn = serial.Serial("COM4",
                             baudrate=9600,
                             bytesize=8,
                             parity='N',
                             stopbits=1)
        data = "FF 01 01 02 EE"
        data = data.split()
        data_hex = []
        for i in range(len(data)):
            data_hex.append(binascii.a2b_hex(data[i]))

        conn.write(data_hex)
        conn.flush()

    # 开灯
    @staticmethod
    def close_light():
        conn = serial.Serial("COM4",
                             baudrate=9600,
                             bytesize=8,
                             parity='N',
                             stopbits=1)
        data = "FF 01 00 01 EE"
        data = data.split()
        data_hex = []
        for i in range(len(data)):
            data_hex.append(binascii.a2b_hex(data[i]))

        conn.write(data_hex)
        conn.flush()
