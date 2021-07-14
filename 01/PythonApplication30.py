#list

hk1=[i for i in range(11,21)]
print(hk1)

hk2=list(range(0,11))
print(hk2)
#新式定义

hk=hk2+hk1
print(hk)
#list加

name=[22,100,41,3,7,10,"xiaoming","xiaoming"]
print(name [6])
#从零编号索引

#另一个list可作为此list元素，元组、字典同理，且三者可互为元素
list1=[1,2,3,4,5]
list=[11,99,100,8987]
list.insert(2,list1)
print(list)

#name.
#加点可以调出可用操做

print(name.index("xiaoming"))
# 求索引    指出第一个

print(name.count("xiaoming"))
#某量出现次数

name[2]="xiyangyang"
print(name)
#修改

name.append("xxx")
print(name)
#末尾添加

name.insert(2,"pure")  # 将新量插入目标索引
print(name)
#插入

name1=["re","te","ppp"]
name.extend(name1)
print(name)
#扩展 新的list

name.remove(22)
print(name)
#用内容清除一个

name.pop(2)
print(name)
#用索引清除一个，若不输入默认删除第一个

name.clear()
print(name)
#清空



