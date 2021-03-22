class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j):
                    if (nums[i]+nums[j] == target):
                        return list(sorted([i,j]))
#Runtime: 44 ms, faster than 85.74% of Python3 online submissions for Two Sum.
#Memory Usage: 14.3 MB, less than 75.08% of Python3 online submissions for Two Sum.
