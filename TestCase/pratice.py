from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def Xpath():
    input_= driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    time.sleep(2)
    input_.send_keys('我于杀戮之中盛放，亦如黎明中的花朵')
    time.sleep(3)
    input_.clear()
    time.sleep(1)

def upload():
    by_id = driver.find_element_by_id('file1')
    time.sleep(2)
    by_id.send_keys('C:/Users/Administrator/Desktop/A日常文件/190508/绘图2.png')
    time.sleep(2)

def single_election():

    name = driver.find_elements_by_name('radio')
    time.sleep(2)
    name[0].click()
    time.sleep(2)
    name[1].click()
    time.sleep(1)

def Multiple_selection():
    class_name = driver.find_elements_by_class_name('checkbox')
    class_name[2].click()
    time.sleep(1)
    class_name[1].click()
    time.sleep(2)
    class_name[0].click()
    time.sleep(1)

def password():
    password_ = driver.find_element_by_xpath('//input[@type="password"]')
    time.sleep(2)
    password_.send_keys('123456')
    time.sleep(1)


def switch():
    action_chains = ActionChains(driver)
    JD_link =driver.find_element_by_link_text('京东')

    action_chains.key_down(Keys.CONTROL).click(JD_link).key_up(Keys.CONTROL).perform()
    time.sleep(3)
    window_handles = driver.window_handles
    for i in window_handles:
        driver.switch_to.window(i)
        if driver.title.__contains__('京东'):
            break

    driver.quit()





if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    # Xpath()
    # single_election()
    # Multiple_selection()
    # password()
    switch()










