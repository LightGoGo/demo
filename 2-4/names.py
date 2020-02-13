# Author : GAO

#name = "aa bb cc dd ee ff"  字符串类型都值不能修改

name = ["aa","bb","cc","dd","ee","ff"]

print(name[0], name[3])



#列表   定义
name = ["aa","bb","cc","dd","ee","ff"]
# 切片
print(name[1:3])  #[:] 切片 前取 后不取
# 追加
name.append("gg")
print(name)
#插入
name.insert(2,"插入1")
print(name)
# 修改
name[2]="nihao"
print(name)
#删除
del name[2]
print(name)
name.remove("gg")
print(name)
name.pop() #删除列表中最后一个值
print(name)

#扩展

bb = [1,2,3]

name.extend(bb)
print(name)
#拷贝

name_c = name.copy()
print(name_c)
#统计个数
print(name.count("dd"))

#获取下标
print(name.index("dd"))

#排序  和  反转
name.sort()
print(name)

name.reverse()
print(name)