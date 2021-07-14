#字典

#无序号的
xiaoming={"age":18,"iq":199,"gender":"nan","hobby":("skate","study")}
print(xiaoming["hobby"])
print(xiaoming)
#别忘了引号

#修正
xiaoming["iq"]=120
print(xiaoming)

#增加
xiaoming["lover"]="xiaohong"
print(xiaoming)

#删除
xiaoming.pop("lover")
print(xiaoming)

#统计字典内项目数量
print(len(xiaoming))

#合并字典，有同样的元素，以新的为准
xiaoming1={"height":180,"age":99}
xiaoming. update(xiaoming1)
print(xiaoming)

#清空
xiaoming.clear()
print(xiaoming)


