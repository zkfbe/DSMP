#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')

class Login(WebPage):
    def click_pass_button(self):
        """跳过google此页面不是安全链接"""
        self.is_click(login['高级按钮'])
        self.is_click(login['继续按钮'])

    def click_ns_login_button(self):
        self.is_click(login['租户登录按钮'])

    def input_nsname(self, nsname):
        self.input_text(login['租户名框'],txt=nsname)

    def click_next_button(self):
        self.is_click(login['下一步按钮'])

    def input_username(self, username):
        """输入账号"""
        self.input_text(login['账号框'],txt=username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(login['密码框'],txt=password)

    def input_verify_code(self, verify_code):
        """输入万能验证码"""
        self.input_text(login['验证码框'],txt=verify_code)

    def click_login_button(self):
        """点击登录按钮"""
        self.is_click(login['登录按钮'])


