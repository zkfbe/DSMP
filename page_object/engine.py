#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

tab = Element('tab')
engine = Element('engine')
sysmange = Element('sysmange')

class Engine(WebPage):

    def click_setting_button(self):
        self.is_click(tab['设置导航栏'])

    def click_sysmange_button(self):
        self.is_click(tab['系统管理导航栏'])

    def click_enginemange_button(self):
        self.is_click(sysmange['引擎管理导航栏'])

    def click_engine_add_button(self):
        self.is_click(engine['添加引擎按钮'])

    def input_engine_tool(self,engine_tool):
        self.is_click(engine['检测工具下拉框'])
        self.is_click_oneofthem(engine['检测工具'],engine_tool)

    def input_engine_name(self,enginename):
        self.input_text(engine['引擎名称框'],enginename)

    def input_engine_version(self,engineversion):
        self.input_text(engine['引擎版本框'],engineversion)

    def input_engine_protocol(self,engineprotocol):
        self.is_click(engine['引擎协议下拉框'])
        self.is_click_oneofthem(engine['引擎协议'],engineprotocol)

    def input_engine_ip(self,engineip):
        self.input_text(engine['引擎IP框'],engineip)

    def input_engine_port(self,engineport):
        self.input_text(engine['引擎端口框'],engineport)

    def input_engine_ak(self,engineak):
        self.input_text(engine['AK框'],engineak)

    def input_engine_sk(self,enginesk):
        self.input_text(engine['SK框'],enginesk)

    def click_send_test(self):
        self.is_click(engine['发送测试按钮'])

    def get_send_test_notice(self):
        return self.element_text(engine['发送测试成功弹窗'])

    def click_sure(self):
        self.is_click(engine['确定按钮'])

    def get_add_notice(self):
        return self.element_text(engine['添加成功弹窗'])









