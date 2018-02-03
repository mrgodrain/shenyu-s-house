import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分', '秒']#单位
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0            #self.start -> begin属性名与方法名相同后,属性名会将方法名覆盖
        self.end = 0

    def __str__(self):            #重写str和repr魔法方法
        return self.prompt

    __repr__ = __str__            #复制

    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    #开始计时
    def start(self):
        self.begin = t.localtime()#time模块的localtime方法获取时间
        self.prompt = '提示:请先调用stop()停止计时!'
        print('计时开始')

    #计时停止
    def stop(self):
        if not self.begin:
            print('提示:请先调用start()进行计时!')
        else:
            self.end = t.localtime()
            self._calc()              #调用内部方法
            print('计时结束')

    #内部方法用 _ ,计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'#提示
        for index in range(6):    #6为时间元祖的索引值,年月日时分秒
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
