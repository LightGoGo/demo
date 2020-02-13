# Author : GAO


#continue 跳出本次循环，进入下一次循环
'''
for i in range(0,10):
    if i < 3:
        print("loop", i )
    else:
        continue
    print("hehe...")


#break 结束本次循环
for i in  range(10):

    print('-------------',i)
    for j in range(10):
        print(j)
        if j > 1 :
            break
'''
#三元运算

a , b ,c = 7,3,5

d= a if a>b else c

print(a,b,c,d)

#bytes类型转换
msg = "我爱北京天安门"

print(msg)
print(msg.encode(encoding="utf-8"))
print(msg.encode().decode())
#b'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'