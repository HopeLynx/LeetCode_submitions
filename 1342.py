class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num:
            if num % 2 == 0 :
                num /= 2
            else:
                num -= 1
            ans += 1
        return ans

# Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 14.1 MB, less than 88.32% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
