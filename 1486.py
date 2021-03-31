class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans = ans ^ (start + 2*i)
        return ans
      
      
# Runtime: 28 ms, faster than 82.50% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 14.1 MB, less than 80.13% of Python3 online submissions for XOR Operation in an Array.
