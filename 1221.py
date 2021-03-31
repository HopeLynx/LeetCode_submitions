class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        balance = 0
        for i in s:
            balance += 1 if  i == "L" else -1
            if balance == 0 :
                ans += 1
        return ans
      
# Runtime: 28 ms, faster than 82.69% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14.3 MB, less than 44.94% of Python3 online submissions for Split a String in Balanced Strings.
