# -*- encoding:utf-8 -*-
__author__ = 'applewu'

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -----------------------
# worked for python 2.7.10, appium 1.3.6
# The following example shows a automated test enter into mini programs from usage history for android.
# Steps: start wechat firstly, click 'Discover', 'Mini Program'..
# How to execute on android device:
# 1. Make sure installed appium-python client and appium had started without any issues;
# 2. Make sure connected android device with your computer;
# 3. Run via the command: python enter_into_mini_programs_ex.py
# -----------------------

your_mini_program = u'哈哈'


def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


desired_caps = {
    'platformName': 'Android',
    'fastReset': 'false',
    'deviceName': 'HKR4C15914023322',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'fullReset': 'false',
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True',
    'chromeOptions': {
        'androidProcess': 'com.tencent.mm:appbrand0'
    }
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.NAME, u'发现')))
driver.find_element_by_name(u"发现").click()

# 对于屏幕小的手机，需要上滑才能看到“小程序”选项
swipeUp(driver)

while (driver.find_elements_by_name(u"小程序").__len__()) > 0:
    driver.find_element_by_name(u"小程序").click()
    driver.find_element_by_name(your_mini_program).click()

driver.implicitly_wait(5)
print(driver.page_source)