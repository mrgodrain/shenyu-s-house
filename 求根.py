import math

def deshu(a,b,c):
    if not (isinstance(a,(int,float))and isinstance(b,(int,float))and isinstance(c,(int,float))):
        raise TabError('bad operand type')

    if a==0:
        if b!=0:
            x1=x2=-b/c
            print(x1,x2)
        elif b==0:
            if c==0:
                print('0=0')
            else:
                print('wujie')
    else:
        D=b*b-4*a*c 
        d=math.sqrt(D)
        if D>=0:
            x1=(-b+d)/(2*a)
            x2=(-b-d)/(2*a)
            print (x1,x2)
        else:
            print('wujie')


a=float(input('输入a：'))
b=float(input('输入b:'))
c=float(input('输入c:'))
deshu(a,b,c)
