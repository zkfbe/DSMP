#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

adminlogin=Element('adminlogin')
admin = Element('admin')

class Admin(WebPage):
    def click_pass_button(self):
        """跳过google此页面不是安全链接"""
        self.is_click(adminlogin['高级按钮'])
        self.is_click(adminlogin['继续按钮'])
    def input_username(self, username):
        """输入账号"""
        self.input_text(adminlogin['账号框'],txt=username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(adminlogin['密码框'],txt=password)

    def input_verify_code(self, verify_code):
        """输入万能验证码"""
        self.input_text(adminlogin['验证码框'],txt=verify_code)

    def click_login_button(self):
        """点击登录按钮"""
        self.is_click(adminlogin['登录按钮'])

    def click_new_ns_button(self):
        """点击新建租户按钮"""
        self.is_click(admin['新建租户按钮'])
    def input_new_ns_name(self,name):
        """新建租户-填写租户名称"""
        self.input_text(admin['租户名称'],txt=name)

    def input_new_ns_adminname(self,adminname):
        """新建租户-填写管理员用户名"""
        self.input_text(admin['管理员用户名'],txt=adminname)

    def input_new_ns_adminpassword(self,adminpassword):
        """新建用户-填写密码"""
        self.input_text(admin['密码'],txt=adminpassword)

    def input_new_ns_confirm_password(self,adminpassword):
        """新建用户-确认密码"""
        self.input_text(admin['确认密码'],txt=adminpassword)

    def click_new_ns_sure(self):
        """新建租户-确定"""
        self.is_click(admin['新建租户确认按钮'])

    def get_new_ns_notice(self):
        return self.element_text(admin['新建租户成功弹窗'])

    def click_reset_button(self):
        """点击重置密码"""
        self.is_click(admin['重置租户密码按钮'])

    def input_reset_adminpassword(self,adminpassword):
        self.input_text(admin['重置密码管理员密码'],txt=adminpassword)

    def input_reset_newpassword(self,newpassword):
        self.input_text(admin['重置密码新密码'],txt=newpassword)

    def input_reset_confirmpassword(self,confirmpassword):
        self.input_text(admin['重置密码确认密码'],txt=confirmpassword)

    def input_reset_verify_code(self,verify_code):
        self.input_text(admin['重置密码验证码'],txt=verify_code)

    def click_reset_sure(self):
        self.is_click(admin['重置密码确定按钮'])

    def get_reset_notice(self):
        return self.element_text(admin['重置密码成功弹窗'])

    def click_delete_button(self):
        """点击删除租户按钮"""
        self.is_click(admin['删除租户按钮'])

    def click_delete_confirm_button(self):
        """点击确认删除按钮"""
        self.is_click(admin['确认删除租户按钮'])

    def get_delete_notice(self):
        return self.element_text(admin['删除成功弹窗'])

