class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        The `merge` function takes a list of intervals and merges overlapping intervals to return a new list of non-overlapping intervals.
        
        :param intervals: The `intervals` parameter is a list of lists, where each sublist represents an interval. Each sublist contains two integers, representing the start and end points of the interval
        :type intervals: list[list[int]]
        :return: a list of merged intervals. Each interval in the list is represented as a sublist of two integers, where the first integer is the start point and the second integer is the end point of the interval.
        """
        res = []
            #  先对数组的进行排序（按照第一个来）
            # The line `nums = sorted(intervals, key = lambda x:x[0])` is sorting the intervals list based on the first element of each sublist. It uses the `sorted()` function with a key parameter to specify the sorting criteria. In this case, the lambda function `lambda x:x[0]` is used as the key, which extracts the first element of each sublist. This ensures that the intervals are sorted in ascending order based on their starting points.
        nums = sorted(intervals, key = lambda x:x[0])
        n = len(nums)
        res.append(nums[0])
        for i in range(1, n):
            if res[-1][1] < nums[i][0]:  # 列表前面的最右端的小于当前区间的最左端，直接将当前 区间加入到结果中
                res.append(nums[i])
            else: # 对应上面的第二种情况
                a, b = res.pop()
                res.append([a, max(b, nums[i][1])])
        return res
solution = Solution()
intervals = [[1,3],[2,6],[8,10],[18,100],[15,18]]
print(solution.merge(intervals))
