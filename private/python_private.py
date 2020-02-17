class Fruit(object):
    #限定Fruit对象只能绑定name，price
    __slots__ = ('_name',"_price")

    def __init__(self, price, name):
        self._price = price
        self._name = name

    #静态方法
    @staticmethod
    def is_fruit(price):
        if price > 999:
            print("this is not fruit,is gold!")

    # 访问器 
    @property
    def name(self):
        return self._name

    # 访问器 
    @property
    def price(self):
        return self._age

    # 修改器 
    @price.setter
    def price(self, price):
        self._price = price

    def judge(self):
        if self._price <= 10:
            print('this %s is cheap,only %s .' % (self._name,self._price))
        else:
            print('this %s is expensive,I pay %s' % (self._name,self._price))


def main():
    fruit = Fruit(15,"apple")
    fruit.judge()
    fruit.price = 7
    fruit.judge()



if __name__ == '__main__':
    main()