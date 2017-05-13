def f1(a,b,c=0,*args,**kw): #可变参数，不变参数，可变关键字参数，关键字参数#
    print("a:",a,"b:",b,'args=',args,'kw=',kw)#f1(1,2,3,'沈宇',m=100)#
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
    #*args是可变参数，args接收的是一个tuple；**kw是关键字参数，kw接收的是一个dict{}#
    
