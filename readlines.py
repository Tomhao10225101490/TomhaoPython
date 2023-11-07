f = open("appendtime.txt","r")
# 1
# print(f.readline())
# print(f.readline())
# # print(f.readline())

# 2
# for line in f.readlines():
    # print(line, end = '')

# 3 "惰性"读取文件法
for line in f:
    print(line,end = '')
#具体区别见01快学P190，或上网查
