import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)#定义坐标
        swlf.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('我的位置是:', self.x, self.y)

class GoldFish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):#覆盖父类
        '''
        Fish.__init__(self)#调用未绑定的父类方法,此处self为子类实例对象
        '''
        super().__init__()#super方法,自动继承父类方法
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃~')
            self.hungry  = False
        else:
            print('太饱了,吃不下!')
