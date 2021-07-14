#高级变量公共操作

#用于字典 元组 list 字符串
a=[1,5,878,"yg","hgiug"]
b=[2,786,98798,5444]
c={1:12,2:7855858,3:67,4:"hfjf"}
d=[1,5,878,"yg","hgiug",1231241,"背景包","hilter"]

print(len(a))
#长度


print (max(b))
print (min(b))
#极值，原有”容器“应全数字
print (max(c))
print (min(c))
#若为字典，比较并输出key


del(a[1])
print(a)
#删除


print(d[3:-2:2])
#切片,方法同49    字典无序，不可用


