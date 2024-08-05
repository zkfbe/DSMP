#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import time

import pytest
from page_object.login import Login
from utils.logger import log
from common.readconfig import ini
from utils.times import sleep


class TestAdmin:

    @pytest.fixture(scope='function',autouse=True)
    def wait(self):
        "每个用例执行完毕等待1s"
        yield
        sleep()

    def test_001(self,drivers):
        """租户登录"""
        login = Login(drivers)
        login.get_url(ini.url)
        login.click_pass_button()
        login.click_ns_login_button()
        login.input_nsname(ini.ns)
        login.click_next_button()
        login.input_username(ini.username)
        login.input_password(ini.password)
        login.input_verify_code(ini.verify_code)
        login.click_login_button()
        text=login.get_url_now()
        assert 'dashboard' in text

    def test_002(self,drivers):
        """添加引擎"""
if __name__ == '__main__':
    pytest.main(['TestCase/test_engine.py'])
