class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]
        for i in range(1,len(nums)):
            running_sum.append(running_sum[i-1]+nums[i])
        return running_sum
#Runtime: 36 ms, faster than 87.46% of Python3 online submissions for Running Sum of 1d Array.
#Memory Usage: 14.5 MB, less than 14.89% of Python3 online submissions for Running Sum of 1d Array.
