class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ex = list()
        ans = 0
        while (len(nums)):
            tmp = nums[0]
            lul = nums.count(tmp)
            while lul > 1:
                lul -= 1
                ans += lul
            ex.append(tmp)
            while tmp in nums:
                nums.pop(nums.index(tmp))
        return ans

#Runtime: 28 ms, faster than 93.02% of Python3 online submissions for Number of Good Pairs.
#Memory Usage: 14.2 MB, less than 73.90% of Python3 online submissions for Number of Good Pairs.
