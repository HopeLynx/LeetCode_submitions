class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for item in nums:
            ans.append(nums[item])
        return ans