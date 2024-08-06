#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import time

import allure
import pytest

from page_object.engine import Engine
from page_object.login import Login
from utils.logger import log
from common.readconfig import ini
from utils.picture_save import save_pic
from utils.times import sleep


@allure.feature('测试引擎管理功能')
class TestAdmin:

    @pytest.fixture(scope='function', autouse=True)
    def wait(self):
        "每个用例执行完毕等待1s"
        yield
        sleep()

    @allure.story('租户登录用例')
    def test_001(self, drivers):
        login = Login(drivers)
        with allure.step('打开DSMP'):
            login.get_url(ini.url)
            login.click_pass_button()
        with allure.step('租户登录'):
            login.click_ns_login_button()
            login.input_nsname(ini.ns)
            login.click_next_button()
            login.input_username(ini.username)
            login.input_password(ini.password)
            login.input_verify_code(ini.verify_code)
            login.click_login_button()
        with allure.step('判断是否登录成功'):
            text = login.get_url_now()
            log.info(text)
            save_pic(drivers)
            assert 'dashboard' in text

    @allure.story('添加引擎用例')
    def test_002(self, drivers):
        """添加引擎"""
        engine = Engine(drivers)
        with allure.step('切换至引擎管理页面'):
            engine.click_setting_button()
            engine.click_sysmange_button()
            engine.click_enginemange_button()
        with allure.step('点击添加引擎按钮'):
            engine.click_engine_add_button()
        with allure.step('填入相关信息'):
            engine.input_engine_tool(ini.scaname)
            engine.input_engine_name(ini.scanewname)
            engine.input_engine_version(ini.scaversion)
            engine.input_engine_protocol(ini.scaprotocol)
            engine.input_engine_ip(ini.scaip)
            engine.input_engine_port(ini.scaport)
            engine.input_engine_ak(ini.scaak)
            engine.input_engine_sk(ini.scask)
        with allure.step('点击发送测试按钮'):
            engine.click_send_test()
        with allure.step('判断是否发送成功'):
            text = engine.get_send_test_notice()
            log.info(text)
            save_pic(drivers)
            assert text == '发送成功'
        with allure.step('点击确定按钮'):
            engine.click_sure()
        with allure.step('判断是否添加成功'):
            text = engine.get_add_notice()
            log.info(text)
            save_pic(drivers)
            assert text == '添加成功'


if __name__ == '__main__':
    pytest.main(['TestCase/test_engine.py'])
