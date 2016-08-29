#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import binascii


class Serial:

    # 十六进制写串口
    @staticmethod
    def write_hex(name, param):
        conn = serial.Serial(name,
                             baudrate=9600,
                             bytesize=8,
                             parity='N',
                             stopbits=1)
        data = param
        data = data.split()
        data_hex = []
        for i in range(len(data)):
            data_hex.append(binascii.a2b_hex(data[i]))

        conn.write(data_hex)
        conn.flush()
