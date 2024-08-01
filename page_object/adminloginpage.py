#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')

class AdminLoginPage(WebPage):
    def input_username(self, username):
        """输入账号"""
        self.input_text(login['账号框'],txt=username)
        sleep()

    def input_password(self, password):
        """输入密码"""
        self.input_text(login['密码框'],txt=password)
        sleep()
