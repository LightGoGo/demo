# Author : GAO

#if-elif-else
'''
_username = 'abc'
_password = '123456'

username = input("username:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome user {name} login ...".format(name=username))
else:
    print("Invalid username or password!")
'''
#当三次都猜不中后，询问是否继续猜
age_of_oldboy = 56
count=0
while count<3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller....")
    else:
        print("think bigger!")
    count += 1

    if count ==3 :
        countine_flag= input("do you want to keep tring..?")
        if countine_flag != 'n':
            count = 0


'''
---int(input("guess age:"))--input是字符类型，需要转换为 数字类型 

Traceback (most recent call last):
  File "/Users/gaominghui/Desktop/python/2-4/fi.py", line 23, in <module>
    elif guess_age > age_of_oldboy:
TypeError: '>' not supported between instances of 'str' and 'int'
'''
