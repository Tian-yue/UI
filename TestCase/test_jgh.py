

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# web_driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
# web_driver.get('https://www.baidu.com/')
#
# def first():
#
#     baidu = web_driver.find_element_by_xpath('//input[@id="kw"]')
#     baidu.send_keys('英雄联盟')
#     time.sleep(2)
# def second():
#     baidu_pratice = ActionChains(web_driver)
#     baiduyx = web_driver.find_element_by_xpath('//*[@id="su"]')
#
#     baidu_pratice.key_down(Keys.CONTROL).click(baiduyx).key_up(Keys.CONTROL).perform()
#     time.sleep(3)
#
#
#     web_driver.quit()
#
#
#
# if __name__ == '__main__':
#
#     first()
#     second()
#
from TestCase.conftest import base
from Common.Baseui import baseUI
import pytest

class Test_ww():



    def test_1(self,base):
        # base.get('https://www.baidu.com/')


        # 输入
        base.send_keys('输入','''//input[@id="kw"]''','''英雄联盟''')
    #     点击百度一下
        base.click('点击','''//*[@id="su"]''')

    pass










