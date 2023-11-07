class Solution:
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans * a % b
            a = a * a % b
            n /= 2
        return ans % b
a = int(input("please input a:"))
n = int(input("please input n:"))
b = int(input("please input b:"))
solution = Solution()
print("output: ",solution.fastPower(a,b,n))