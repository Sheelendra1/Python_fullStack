# y = lambda x: x**2
# print(y(5))


# def sum(a, b):
#     return a+b
# print(sum(2,3))

# x=lambda a,b:a+b
# print(x(2,3))

# max = lambda a, b: a if a > b else b
# print(max(2,3))


list1 = [1,2,3,4,5]
res=[]
for i in list1:
    res.append((i*i))
print(res)


z=list(map(lambda x: x**2,list1))
print(z)

z=list(filter(lambda x: x%2==0,list1))
print(z)

from functools import reduce
z = reduce(lambda x, y:x+y,list1)
print(z)

f=lambda x: x+3
print(f(5))