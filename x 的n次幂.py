#实现Pow(x,n),计算并返回x的n次幂
#x为double类型的
#n为整数的
#返回值为double类型
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        tmp = x
        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //= 2
        return ans
temp = Solution()
num1 = float(input("num1: "))
num2 = float(input("num2: "))
print("num1: ",num1,' ',"nums2: ",num2)
print("result: ",str(temp.myPow(num1, num2)))