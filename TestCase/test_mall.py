from time import sleep

from Common.Baseui import baseUI
import pytest

from TestCase.pages import order_list


class Test_mall():
    # def test_login(self,driver):
    #     # 使用baseUI
    #     base = baseUI(driver)
    #     # 打开登录页面
    #     driver.get('http://192.168.60.132/#/login')
    #     # 输入用户名
    #     base.send_keys('输入用户名','//input[@name="username"]','admin')
    #     # 输入密码
    #
    #     base.send_keys('输入密码','//input[@name="password"]','123456')
    #     # 点击登录
    #     # w = driver.find_element_by_class_name('el-button el-button--primary')
    #     # w.click()
    #     base.click('点击登录','//span[contains(text(),"登录")]')
    #     assert '首页' in driver.page_source
    #     sleep(2)

    @pytest.mark.fh
    def test_fh(self,base):
        base.driver.get("http://192.168.60.132/#/oms/order")

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



        # 点击订单状态
        # order_list1.click_order_status_a()
        # # 点击待发货
        # order_list1.click_To_be_shipped()
        # # 点击查询搜索
        # order_list1.click_Query_Search()
        # # 点击订单发货
        # order_list1.click_Order_delivery()


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
        text= base.get_text("断言", '''//div[@class="el-message el-message--success"]//p''')

        print(type(text))
        assert "发货成功" in text
        pass
    @pytest.mark.return_goods
    def test_return_goods(self,base):

        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        # 点击退货申请//a[@href="#/oms/returnApply"]//li//span
        base.click('点击退货申请', '//a[@href="#/oms/returnApply"]//li//span')
        sleep(2)
        # 点击处理状态//label[contains(text(),'处理状态')]//following-sibling::div//i
        # base.click('点击处理状态', '//label[contains(text(),"处理状态")]//following-sibling::div//i')
        # base.click('选择处理状态','''//span[@class="el-input__suffix"]''')
        base.click('选择处理状态', '''//label[contains(text(),'处理状态')]/following-sibling::div//input''')
        sleep(2)
        # 选择待处理//span[contains(text(),'待处理')]
        base.click('选择待处理', '//span[contains(text(),"待处理")]')
        sleep(2)
        # 端机查询搜索//span[contains(text(),'筛选搜索')]//following-sibling::button[1]//span
        base.click('查询搜索', '//span[contains(text(),"筛选搜索")]//following-sibling::button[1]//span')
        sleep(2)
        # 点击查看详情//tbody//tr[@class="el-table__row"]//td[8]//span
        base.click('点击查看详情', '//tbody//tr[@class="el-table__row"]//td[8]//span')
        sleep(2)
        # 滚动窗口至最下面
        base.scroll_screen("滚动窗口至最下面")
        sleep(2)
        # 获取订单金额//div[contains(text(),'订单金额')]/following-sibling::div
        money = base.get_text('获取订单金额', '//div[contains(text(),"订单金额")]/following-sibling::div')
        money_ = money[1:]
        sleep(2)
        # 输入退款金额//div[contains(text(),'确认退款金额')]/following-sibling::div//input
        base.send_keys('输入退款金额', '//div[contains(text(),"确认退款金额")]/following-sibling::div//input',str(money_))
        sleep(2)
        # 选择收货点
        # 添加备注
        # 点击确认退货//span[contains(text(),'确认退货')]
        base.click('点击确认退货', '//span[contains(text(),"确认退货")]')
        sleep(2)
        # 点击确定//div[@class="el-message-box"]//button[2]//span
        base.click('点击确定', '//div[@class="el-message-box"]//button[2]//span')

        # 获取操作成功文本//div[@role="alert"]//p
        actual = base.get_text("获取操作提示文本", '''//div[@role="alert"]//p''')

        # 断言
        assert '操作成功' in actual
        pass















