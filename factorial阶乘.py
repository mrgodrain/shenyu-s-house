def factorial(x):
    for i in range(1,x):
        x = x * i
    return x

number = int(input("请输入要阶乘的数:"))
print(factorial(number))
