class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_s = 0
        for item in accounts:
            max_s = max(max_s,sum(item))
        return max_s
#Runtime: 56 ms, faster than 49.75% of Python3 online submissions for Richest Customer Wealth.
#Memory Usage: 14.2 MB, less than 61.30% of Python3 online submissions for Richest Customer Wealth.
