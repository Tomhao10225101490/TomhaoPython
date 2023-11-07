
x1 = {"tom", "Amy","Bob"}
# `student1 = dict.fromkeys(x1)` is creating a dictionary called `student1` where the keys are the elements in the set `x1` and the values are set to `None` by default.
student1 = dict.fromkeys(x1)
print(student1)
 

x2 = ("tom","Amy","Bob")
# `student2 = dict.fromkeys(x2,18)` is creating a dictionary called `student2` where the keys are the elements in the tuple `x2` and the values are set to `18` for all keys.
student2 = dict.fromkeys(x2,18)
print(student2)
print(student2.keys())
print(student2.values())
print(student2.items())

for k, v in student2.items():
    print(k , " ages ",v)