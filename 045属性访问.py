'''
class C:
    def __getattribute__(self, name):        #比getattr先
        print('getattribute')
        return super().__getattribute__(name)#super自动查找基类
    def __getattr__(self, name):
        print('getattr')
    def __setattr__(self, name, value):
        print('setattr')
        super().__setattr__(name,value)
    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(self, name)

c = C()
c.x
c.x = 1
del c.x
'''
class Rectangle:
    def __init__(self, width=0, height=0):#此处赋值出发attr,进而触发else
        self.width = width
        self.hight = height
    def __setattr__(self, name, value):
        if name == 'aquare':
            self.width = value
            self.height = value
        else:
            super().__setattr__(name, value)#调用基类/self.__dict__[name]=value

    def getArea(self):
        return self.width * self.height

r1 = Rectangle(4, 5)
r1.getArea
r1.square = 10
r1.width
r1.height
r1.getArea
