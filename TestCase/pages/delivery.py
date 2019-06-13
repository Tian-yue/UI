class delivery():
    # 选择物流公司
    Logistics_company = '// input[ @ placeholder = "请选择物流公司"]'
    # 选择物流
    Choosing_Logistics = '//span[contains(text(),"中通快递")]'
    # 输入物流单号
    Input_Logistics_Number = '//div[@class="el-input el-input--small"]//input'
    # 点击确定
    Click_OK = '//button[@class="el-button el-button--primary"]//span'
    # 点击确定发货
    Confirmation_of_delivery = '//div[@class="el-message-box__btns"]/button[2]//span'
    # 断言
    assertion = '''//div[@class="el-message el-message--success"]//p'''

    def cilck_Logistics_company(self):










    base.click('选择物流', '// input[ @ placeholder = "请选择物流公司"]')
    base.click('选择物流', '//span[contains(text(),"中通快递")]')
    # 输入物流单号
    base.send_keys('输入物流单号', '//div[@class="el-input el-input--small"]//input', '23333336456441')

    # 点击确定
    base.click('订单发货', '//button[@class="el-button el-button--primary"]//span')
    sleep(3)
    # 点击确定
    base.click('订单发货', '//div[@class="el-message-box__btns"]/button[2]//span')
    # 断言
    # base.get_text('断言', '//p[constains(text(),"发货成功")]')
    text = base.get_text("断言", '''//div[@class="el-message el-message--success"]//p''')
    pass