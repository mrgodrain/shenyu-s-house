
#递归法(慢)
def Fab(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fab(n-1) + Fab(n-2)
number = int(input("请输入n的值:" ))
result = Fab(number)
print ('%d的斐波那契数是%d' %(number,result))




'''
迭代法(快)

def Fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n<1:
        print('输入错误!')

    while n>2:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n-=1        #循环次数减一
    return n3
        
number = int(input("请输入n的值:" ))
result = Fab(number)
print ('%d的斐波那契数是%d' %(number,result))
'''
