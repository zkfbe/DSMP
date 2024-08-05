#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser
from config.conf import cm
from utils.randomname import random_name

HOST = 'HOST'
USER = 'USER'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
VERIFY_CODE = 'VERIFY_CODE'
NS = 'NS'
NEWPASSWORD = 'NEWPASSWORD'

class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    @property
    def username(self):
        return self._get(USER, USERNAME)

    @property
    def password(self):
        return self._get(USER, PASSWORD)
    @property
    def verify_code(self):
        return self._get(VERIFY_CODE, VERIFY_CODE)

    @property
    def newns(self):
        return self._get(USER, NS) + random_name()

    @property
    def ns(self):
        return self._get(USER, NS)

    @property
    def newpassword(self):
        return self._get(USER, NEWPASSWORD)
ini = ReadConfig()

if __name__ == '__main__':
    print(ini.ns)
