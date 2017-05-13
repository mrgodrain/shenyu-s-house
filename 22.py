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
