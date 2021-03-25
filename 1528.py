class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = len(s)
        x = [0]*tmp
        for i in range(tmp):
            x[indices[i]] = s[i]
        return ''.join(x)
      
# Runtime: 40 ms, faster than 99.82% of Python3 online submissions for Shuffle String.
# Memory Usage: 14.3 MB, less than 23.04% of Python3 online submissions for Shuffle String.
