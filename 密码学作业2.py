
s1 = [[14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7],
      [ 0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8],
      [ 4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0],
      [15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13]]

def fun1(num):
    num1 = (num//32)*2 + (num&1)
    print('num1',num1)
    num2 = (num&30)//2
    print('num2',num2)
    return s1[num1][num2]


def partial_pairs_xor_distribution_table_S1():
    table = [[0] * 16 for _ in range(64)]  # 创建一个64x16的表格，初始值为0
    
    for x in range(64):
        for i in range(64):
            son = x^i
            temp1 = fun1(i)
            temp2 = fun1(son)
            outer = temp1^temp2
            print(outer)
            table[x][outer] += 1
    
    return table

#  调用函数生成S1的部分对XOR分布表
table_S1 = partial_pairs_xor_distribution_table_S1()

# 打印表格
for row in table_S1:
    print(row)