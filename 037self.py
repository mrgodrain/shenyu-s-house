'''
#self与__init__
class Ball:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print('我叫%s,该死的,谁踢我..' %self.name)

c = Ball('土豆')

print(str(c.kick)) 

'''

#定义私有变量
class Person:
    __name = 'hey宇'
    def getName(self):
        return self.__name

p = Person()
print(str(p.getName()))#通过内部方法访问

print(str(p._Person__name))#直接访问(python为伪私有变量)
