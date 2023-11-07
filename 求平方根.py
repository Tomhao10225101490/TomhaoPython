class Solution:
    def mysqrt(self, x):
        l, r = 0, x
        while l + 1 < r:
            mid = (r+l) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid
        if r * r == x:
            return r
        else:
            return l
temp = Solution()
num = int(input("your num: "))
print("the sqrt of ",num," is",str(temp.mysqrt(num)))