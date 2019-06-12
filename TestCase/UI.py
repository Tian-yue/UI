from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    #通过选择复制xpath访问:
    # time.sleep(1)
    # Xpath = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    #
    # Xpath.send_keys('艾欧尼亚昂扬不灭')
    # time.sleep(1)
    #
    # Xpath.clear()
    # time.sleep(1)
    #
    #  通过ID定位,用绝对路径
    # element_id = driver.find_element_by_id('file1')
    # element_id.send_keys('C:/Users/Administrator/Desktop/A日常文件/190509/状态迁移图.png')
    # time.sleep(1)
    #
    #  定位元素,通过name定位
    # element_name = driver.find_elements_by_name('radio')
    # print(type(element_name))
    # element_name[0].click()
    # element_name[1].click()
    # time.sleep(3)
    # driver.quit()


    # 通过class定位
    # class_name = driver.find_elements_by_class_name('checkbox')
    # class_name[0].click()
    # time.sleep(3)
    # class_name[1].click()
    # time.sleep(3)
    # class_name[2].click()
    # time.sleep(3)

    # 用相对路径
    # button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    # button_el.click()
    #
    # driver.switch_to.alert.accept()

    # driver.switch_to.alert.dismiss()


    # 用相对路径
    # by_xpath = driver.find_element_by_xpath('//input[@type="password"]')
    # time.sleep(3)
    # by_xpath.send_keys('123456')
    # time.sleep(3)
    # by_xpath.clear()
    # time.sleep(3)

    # selector = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    # select = Select(selector)
    # select.select_by_index(2)
    # time.sleep(3)
    # select.select_by_value('z2')
    # time.sleep(3)
    # select.select_by_visible_text('周龙1')
    # time.sleep(3)
    #

    # driver.find_element_by_xpath('//select[@value="z1"]')

    # 超链接
    driver.find_element_by_link_text('当当').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element_by_partial_link_text('娘').click()
    time.sleep(2)

    driver.refresh()
    time.sleep(2)

    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element_by_link_text('京东').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)


    






    driver.quit()