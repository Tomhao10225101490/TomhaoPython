#list 
x1 = [1,2,3]*5
print("list")
print(x1)
#tuple
x2 = (1,2,3)*5
print("tuple")
print(x2)
#tuple again another way
_x = (1,2,3,)*5
print("the tuple with the  common")
print(_x)
#string 
x3 = "123456"*5
print("string")
print(x3)
print(max(x3))
print(sum(x2))
print(x1[::-1])#类似于reverse，但reverse方法修改原来的序列，并且没有返回值
print("reverse of x1")
print(x1.reverse())#no return value ,None
print(x1) #the x1 is reversed already