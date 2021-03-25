class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        t = len(stones)
        sum = 0
        while t:
            if stones[t-1] in jewels:
                sum += 1
            t -= 1
        return sum
# Runtime: 24 ms, faster than 95.18% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.1 MB, less than 75.59% of Python3 online submissions for Jewels and Stones.
