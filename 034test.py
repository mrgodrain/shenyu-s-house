#素数:除了1和它本身以外不再有其他因数
while True:
    def showMaxFactor(num):
        count = num //2    #非精确
        while count >1:
            if num % count == 0:
                print("%d的最大约数是%d:"%(num,count))
                break
            count -= 1
        else:
            print('%d是素数!' % num)
    num = int(input('请输入一个数:'))	
    showMaxFactor(num)
