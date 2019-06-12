from time import sleep

from Common.Baseui import baseUI


class Test_mall():
    def test_login(self,driver):
        # 使用baseUI
        base = baseUI(driver)
        # 打开登录页面
        driver.get('http://192.168.60.132/#/login')
        # 输入用户名
        base.send_keys('输入用户名','//input[@name="username"]','admin')
        # 输入密码

        base.send_keys('输入密码','//input[@name="password"]','123456')
        # 点击登录
        # w = driver.find_element_by_class_name('el-button el-button--primary')
        # w.click()
        base.click('点击登录','//span[contains(text(),"登录")]')
        assert '首页' in driver.page_source
        sleep(1)


    def test_fh(self,driver):
        base = baseUI(driver)
        # 点击订单
        base.click('点击订单','//span[contains(text(),"订单")]')
        # 点击订单列表
        base.click('订单列表', '// span[contains(text(), "订单列表")]')

        # 点击订单状态
        base.click('订单状态', '//label[contains(text(),"订单状态：")]/following-sibling::div//input')


        # 点击待发货
        base.click('待发货', '//span[contains(text(),"待发货")]')
        sleep(3)

        # 点击查询搜索
        base.click('查询搜索', '// span[contains(text(), "查询搜索")]')
        sleep(3)
        # 点击订单发货
        base.click('订单发货', '// span[contains(text(), "订单发货")]')
        sleep(3)
        # 选择物流
        base.click('选择物流', '// input[ @ placeholder = "请选择物流公司"]')
        base.click('选择物流', '//span[contains(text(),"中通快递")]')
        # 输入物流单号
        base.send_keys('输入物流单号','//div[@class="el-input el-input--small"]//input','23333336456441')

        # 点击确定
        base.click('订单发货', '//button[@class="el-button el-button--primary"]//span')
        sleep(3)
        # 点击确定
        base.click('订单发货', '//div[@class="el-message-box__btns"]/button[2]//span')
        # 断言
        # base.get_text('断言', '//p[constains(text(),"发货成功")]')
        # base.get_text("断言", '''//div[@class="el-message el-message--success"]//p''')
        local_element = base.local_element('//div[@class="el-message el-message--success"]//p')
        print(type(local_element))
        assert local_element.text in driver.page_source
        pass

