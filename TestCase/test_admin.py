#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import time

import pytest
import allure
from page_object.admin import Admin
from utils.logger import log
from common.readconfig import ini
from utils.picture_save import save_pic
from utils.times import sleep


@allure.feature('测试超管功能')
class TestAdmin:

    @pytest.fixture(scope='function', autouse=True)
    def wait(self):
        "每个用例执行完毕等待1s"
        yield
        sleep()

    @allure.story('管理员登录用例')
    def test_001(self, drivers):
        login = Admin(drivers)
        with allure.step('打开DMSP'):
            login.get_url(ini.url)
            login.click_pass_button()
        with allure.step('输入账号、密码、验证码'):
            login.input_username(ini.username)
            login.input_password(ini.password)
            login.input_verify_code(ini.verify_code)
        with allure.step('点击登录'):
            login.click_login_button()
        with allure.step('判断是否登录成功'):
            result = login.get_url_now()
            log.info(result)
            save_pic(drivers)
            assert 'listada' in result


    @allure.story('管理员新建租户用例')
    def test_002(self, drivers):
        new_ns = Admin(drivers)
        with allure.step('点击新建租户按钮'):
            new_ns.click_new_ns_button()
        with allure.step('填入相关信息'):
            new_ns.input_new_ns_name(ini.newns)
            new_ns.input_new_ns_adminname(ini.username)
            new_ns.input_new_ns_adminpassword(ini.password)
            new_ns.input_new_ns_confirm_password(ini.password)
        with allure.step('点击确认'):
            new_ns.click_new_ns_sure()
        with allure.step('判断是否登录成功'):
            text = new_ns.get_new_ns_notice()
            log.info(text)
            save_pic(drivers)
            assert text == '新建成功'


    @allure.story('管理员重置租户密码用例')
    def test_003(self, drivers):
        reset = Admin(drivers)
        with allure.step('点击重置密码按钮'):
            reset.click_reset_button()
        with allure.step('填入相关信息'):
            reset.input_reset_adminpassword(ini.password)
            reset.input_reset_newpassword(ini.newpassword)
            reset.input_reset_confirmpassword(ini.newpassword)
            reset.input_reset_verify_code(ini.verify_code)
        with allure.step('点击确定'):
            reset.click_reset_sure()
        with allure.step('判断是否重置成功'):
            text = reset.get_reset_notice()
            log.info(text)
            save_pic(drivers)
            assert text == "密码重置成功！"


    @allure.story('管理员删除租户用例')
    def test_004(self, drivers):
        delete = Admin(drivers)
        with allure.step('点击删除租户按钮'):
            delete.click_delete_button()
        with allure.step('点击二次确定按钮'):
            delete.click_delete_confirm_button()
        with allure.step('判断是否删除成功'):
            text = delete.get_delete_notice()
            log.info(text)
            save_pic(drivers)
            assert text == '删除成功'



if __name__ == '__main__':
    pytest.main(['-vs', 'TestCase/test_admin.py', '--clean-alluredir', '--alluredir=reports/allurefile'])
