class order_list():
    def __init__(self,base):
        self.base = base
    # 订单状态
    order_status_a = '''//label[contains(text(),"订单状态：")]/following-sibling::div//input'''
    # 待发货
    To_be_shipped = '''//span[contains(text(),"待发货")]'''
    # 查询搜索
    Query_Search = '''// span[contains(text(), "查询搜索")]'''
    # 订单发货
    Order_delivery = '''// span[contains(text(), "订单发货")]'''



    def click_order_status_a(self):
        self.base.click('订单状态',self.order_status_a)

    def click_To_be_shipped(self):
        self.base.click('待发货',self.To_be_shipped)
    def click_Query_Search(self):
        self.base.click('查询搜索',self.Query_Search)
    def click_Order_delivery(self):
        self.base.click('订单发货',self.Order_delivery)
















    pass
