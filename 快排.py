class Solution:
    def sortIntegers(self,A):
        self.quickSort(A,0,len(A)-1 )
    def quickSort(self,A,start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = A[(start + end) // 2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1   #都向中间运动
            if left <= right:
                A[left],A[right] = A[right],A[left]
                left += 1
                right -= 1
        self.quickSort(A,start, right)
        self.quickSort(A,left, end)
#mian
A = [3,4,2,1,6,5]
print("the prime array A is ",A)
solution = Solution()
solution.sortIntegers(A)
print("after the quicksort ,A is ",A)
                