#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import subprocess



def main():
    """主函数"""
    steps = [
        "source ~/.bash_profile",
        "pytest --alluredir ./report/result --clean-alluredir",
        "allure generate ./report/result -c -o allure-report",
        "allure open allure-report"
    ]
    for step in steps:
        subprocess.run(step, shell=True)


if __name__ == "__main__":
    main()
