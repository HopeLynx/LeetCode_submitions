class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = list()
        for i in  range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
#Runtime: 56 ms, faster than 87.81% of Python3 online submissions for Shuffle the Array.
#Memory Usage: 14.2 MB, less than 98.97% of Python3 online submissions for Shuffle the Array.
