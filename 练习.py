Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('1+2=','1+2')
1+2= 1+2
>>> print('1+2=',1+2)
1+2= 3
>>> name=input()
shenyu
>>> name
'shenyu'
>>> name=input()
shenyu
>>> print('hello',name)
hello shenyu
>>> name=input('please enter your name')
please enter your nameshenyu
>>> print('heelo',name)
heelo shenyu
>>> print('i\'m leraning\npython')
i'm leraning
python
>>> print(r'i'm learning python')
      
SyntaxError: invalid syntax
>>> print('''i ''')
i 
>>> print('''i am learning python''')
i am learning python
>>> print('''i am
learning
python''')
i am
learning
python
>>> python
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> 3>2
True
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> chr(102)
'f'
>>> chr(111111111)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    chr(111111111)
ValueError: chr() arg not in range(0x110000)
>>> chr(9292)
'\u244c'
>>> chr('宇')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    chr('宇')
TypeError: an integer is required (got type str)
>>> ord('宇')
23431
>>> ord（‘沈’）
SyntaxError: invalid character in identifier
>>> ord('沈')
27784
>>> '中午'encode('etf-8')
SyntaxError: invalid syntax
>>> '中文'.encode(''utf-8)
SyntaxError: invalid syntax
>>> 'ABC'encode('ascii')
SyntaxError: invalid syntax
>>> 'ABC'.encode('sacii')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    'ABC'.encode('sacii')
LookupError: unknown encoding: sacii
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
>>>  'ABC'.encode('ascii')
 
SyntaxError: unexpected indent
>>> 'ABC'.encode('ascii')
b'ABC'
>>> b'ABC'
b'ABC'
>>> 
>>> 'hello,%s'%'world'
'hello,world'
>>> 'hi,%s,you have $%d'%('shenyu',10000)
'hi,shenyu,you have $10000'
>>> s1=72
s2=85
r=(s2-s1)/s1*100
print("提升%0.1f%%"%r)
SyntaxError: multiple statements found while compiling a single statement
>>> age=3
>>> if age>18
SyntaxError: invalid syntax
>>> if age>=18:
	print('adult')SyntaxError: invalid synta
	
SyntaxError: invalid syntax
>>> age=24
>>> if age>=18:
	print('adult')
    else age>=6
    
SyntaxError: unindent does not match any outer indentation level
>>>  age=24
>>> if age>=18:
	print('adult')
    else age>=6
    
SyntaxError: unexpected indent
>>> age=24
>>> if age>=18:
	print('adult')
    else age>=6:
	    
SyntaxError: multiple statements found while compiling a single statement
>>> age=24
>>> if age>=18:
	print("adult")
	else age>=6:
		
SyntaxError: invalid syntax
>>> age=24
>>> if age>=18:
	print("adult")
    elif age>=6:
	    
SyntaxError: unindent does not match any outer indentation level
>>> age = 3
if age >= 24:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
SyntaxError: multiple statements found while compiling a single statement
>>> age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
