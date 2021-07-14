#for字典

xiaoming={"age":"18","iq":"199","gender":"nan","hobby":("skate","study")}
for k in xiaoming:
    print("%s : %s"%(k,xiaoming[k]))
#  k 代表了字典中的key,如age,iq
print(xiaoming["age"])