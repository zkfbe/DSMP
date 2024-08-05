#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import time

import pytest
from page_object.admin import Admin
from utils.logger import log
from common.readconfig import ini
from utils.times import sleep


class TestAdmin:

    @pytest.fixture(scope='function',autouse=True)
    def wait(self):
        "每个用例执行完毕等待1s"
        yield
        sleep()

    def test_001(self, drivers):
        """管理员登录"""
        login = Admin(drivers)
        login.get_url(ini.url)
        login.click_pass_button()
        login.input_username(ini.username)
        login.input_password(ini.password)
        login.input_verify_code(ini.verify_code)
        login.click_login_button()
        result = login.get_url_now()
        assert 'list' in result

    def test_002(self, drivers):
        """新建租户"""
        new_ns = Admin(drivers)
        new_ns.click_new_ns_button()
        new_ns.input_new_ns_name(ini.newns)
        new_ns.input_new_ns_adminname(ini.username)
        new_ns.input_new_ns_adminpassword(ini.password)
        new_ns.input_new_ns_confirm_password(ini.password)
        new_ns.click_new_ns_sure()
        text = new_ns.get_new_ns_notice()
        assert text == '新建成功'

    def test_003(self, drivers):
        """重置租户密码"""
        reset=Admin(drivers)
        reset.click_reset_button()
        reset.input_reset_adminpassword(ini.password)
        reset.input_reset_newpassword(ini.newpassword)
        reset.input_reset_confirmpassword(ini.newpassword)
        reset.input_reset_verify_code(ini.verify_code)
        reset.click_reset_sure()
        text = reset.get_reset_notice()
        assert text == "密码重置成功！"


    def test_004(self, drivers):
        """删除租户"""
        delete = Admin(drivers)
        delete.click_delete_button()
        delete.click_delete_confirm_button()
        text = delete.get_delete_notice()
        assert text == '删除成功'


if __name__ == '__main__':
    pytest.main(['TestCase/test_admin.py'])
