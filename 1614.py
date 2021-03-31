class Solution:
    def maxDepth(self, s: str) -> int:
        max_i = -1
        tmp = 0
        for i in s:
            if i == "(":
                tmp += 1
            elif i == ")":
                tmp -= 1
            if tmp > max_i:
                max_i = tmp
        return max_i
    
    
    
# Runtime: 24 ms, faster than 94.92% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
# Memory Usage: 14 MB, less than 89.38% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
