height = float(input('小明的身高：'))
weight = float(input('小明的体重：'))
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print('体重过轻')
elif bmi < 25: 
    print('体重正常')
elif bmi < 28:
    print('体重过重')
elif bmi < 32:
    print('体重肥胖')
else:
    print('体重严重肥胖')







g=float(input('输入你的身高:'))
z=float(input('输入你的体重:'))
BMI=z/(g*g)
if BMI<18.5:
    print('过轻')
elif 18.5<BMI and BMI<=25:
    print('正常')
elif BMI>25:
    print('过重')
