class Solution:
    def checkPowerOf2(self, n):
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans = ans<<1
        return False
temp = Solution()
nums1 = 16
nums2 = 17
print("the nums1 is: ",str(nums1))
print("the ans of nums1 is: ",str(temp.checkPowerOf2(nums1)))
print("the nums2 is: ",str(nums2))
print("the ans of nums2 is: ", str(temp.checkPowerOf2(nums2)))
