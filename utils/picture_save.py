import allure


def save_pic(driver):
    driver.get_screenshot_as_file("./temp/temp_pic.png")
    # 将上一步的截图附加进测试报告
    allure.attach.file("./temp/temp_pic.png", attachment_type=allure.attachment_type.PNG)