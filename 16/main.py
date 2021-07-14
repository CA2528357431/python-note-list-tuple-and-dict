#enumerate

a=['a','b','c']
for x,y in enumerate(a):
    print(x,"  ",y)
print('1-----')
a=('a','b','c')
for x,y in enumerate(a):
    print(x,"  ",y)
print('2-----')
a={'a','b','c'}
for x,y in enumerate(a):
    print(x,"  ",y)
print('3-----')

#转化为[(index,value),(index,value),(index,value)]


a={'a':5,'b':7,'c':9}
for x,y in enumerate(a):
    print(x,"  ",y,'   ')
print('4-----')

#转化为[(index,key),(index,key),(index,key)]