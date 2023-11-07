class Solution:
    #完全平方数的判别函数
    def isPerfectSquare(self, num):
        l = 0
        r = num
        while(r - l > 1):
            mid = (l + r)//2
            if(mid * mid <= num):
                l = mid
            else:
                r = mid
        ans = l
        if(l * l < num):
            ans = r
        print(ans)
        return ans * ans == num
num = int(input("the num is :"))
# num = 25
print("the prime num: ", num)
solution = Solution()
print("the result: ",solution.isPerfectSquare(num))
