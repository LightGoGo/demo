# Author : GAO

print("hello world")

# 变量  （为了多次调用，先存放到一个地方；）  变量存在内存里
# 变量 直接关联 数值
# 变量定义的规则：1。变量名只能是字母，数字或下划线的任意组合 2。第一个字符不能是数字，关键字不能声明为变量
# 大写变量是常量

name = "Gao MingHui"
name2 = name
print("My name is", name, name2)

name = "PaoChe"
print(name,name2)

# 查询哪些关键字 ?
#import keyword
#keyword.kwlist
'''
在这个工具中查询不出来，
直接从IDLE中能查询
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#字符编码  计算机底层是 0  1
'''
二进制  转换  数字
ASCII 美国标准信息交换代码 1字节 8位 最多255个符号  西方用来127  2**8-1 255
GB2312  1980年 7xxx多汉字
GBK1.0   1995  2w多
GB18030   2000  27xxx
unicode 万国码   2字节bytes 16位
UTF-8   可动态变长的字符集 英文1个字节 中文字符是 3个字节
'''

#三个引号  多行注释，打印多行   单引号和双引号功能一样。

aa = '''
hello word,
woshi 'gao'
'''
print(aa)

#-----------------------------------------
#用户输入


username = input("username:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")



info = '''
----------info of %s------------
name: %s
age : %d
job : %s
salary: %s 

''' % (username,username,age,job,salary)
print(info)