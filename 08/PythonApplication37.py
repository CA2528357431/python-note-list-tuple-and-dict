#元组 函数 与 格式
def fx(x,y):
    n="xxx"
    a=x*5+y**4
    return n,a

x=["xm",19]

l=fx(1,2)

print(type (l))
print("woshi %s jinnian %d"%l)
print("woshi %s jinnian %d"%x)

#是  元组   而非list 可用于格式
#函数多个输出时，接受的是元组