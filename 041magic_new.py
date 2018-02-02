class CapStr(str):#继承str,str不可修改类型,无法用init修改
    def __new__(cls, string):
        string1 = string.upper()#new的时候重写,调用字符串的内置方法
        return str.__new__(cls, string1)#return一个实例化对象,先把内容变了,再构造一次传回去

a = CapStr("hey, yu!")
print(a)
