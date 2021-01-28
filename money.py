"""
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额


"""


class Money:
    pass

    def __init__(self):
        # 原有存款1000元
        self.save_money = 1000

        # 定义发工资模块send_money，通过传参来增加收入

    def send_money(self, send_money):
        self.send_money = send_money

    # 定义工资查询模块select_money，用来展示工资数额
    def select_money(self):
        self.select_money = self.save_money + self.send_money
        print(self.select_money)


if __name__ == '__main__':
    money = Money()
    money.send_money(1000)
    money.select_money()
