class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(index[i],nums[i])
        return ans

# Runtime: 32 ms, faster than 77.06% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 14.3 MB, less than 49.25% of Python3 online submissions for Create Target Array in the Given Order.

