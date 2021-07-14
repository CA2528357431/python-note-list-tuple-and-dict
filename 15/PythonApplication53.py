# 字典与for

a={"name":"A","iq":99,"grade":600}
b={"name":"B","iq":199,"grade":800}
c={"name":"C","iq":159,"grade":1000}
list=[a,b,c]

name=input("name,please")
for x in list:
    if x["name"]==name:
        print(x)
        break
else:
    print("无此人")