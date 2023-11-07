empty = set()
print("empty set ",empty )
number = {1,2,3}
_number = {}
print(type(number))
print(type(_number))
print("number set ", number)
mix = set([1,'hello',3.14])
print(type(mix))
print("mix set ", mix)

number.add(5)
print(number)
number.add(2)
print(number)
number.remove(3)
print(number)
number.remove(5)
print(number)

num1 = {1,2,3,4,5}
num2 = {0,2,3,5,6,"hello"}
#并集
print("并集",num1 & num2)
print("交集", num1|num2)
print("差集", num1 - num2 )
print("对称差集" , num1 ^ num2)