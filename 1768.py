class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        inv = False
        if len(word1) > len(word2):
            word1, word2 = word2, word1
            inv = True
        ans = ""
        for i in range(0, len(word1)):
            if not inv:
                ans += word1[i]
                ans += word2[i]
            else:
                ans += word2[i]
                ans += word1[i]
        return ans + word2[len(word1):]

# Runtime: 31 ms Beats 81.48% of users with Python3
# Memory Usage: 16.51 MB Beats 52.92% of users with Python3
