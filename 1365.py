class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        tmp = len(nums)
        for i in range(tmp):
            nums[i] = x.index(nums[i])
        # x.clear()
        return nums
      
# Runtime: 64 ms, faster than 71.21% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14.2 MB, less than 76.52% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
