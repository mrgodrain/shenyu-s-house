class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)#组合:类的实例化放到一个新类里面
        self.fish = Fish(y)

    def print_num(self):
        print('水池里一共%d只乌龟,%d只鱼'%(self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.print_num()
