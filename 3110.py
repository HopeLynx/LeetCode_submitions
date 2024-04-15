class Solution:
    def scoreOfString(self, s: str) -> int:
        score = abs(ord(s[0]) - ord(s[1]))
        for i in range(1, len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score

# Runtime: 33 ms Beats 100.00% of users with Python3
# Memory Usage: 16.52 MB Beats 100.00% of users with Python3
