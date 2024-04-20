class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(0,len(words)):
            if x in words[i]:
                ans.append(i)
        return ans



# Runtime: 62 ms Beats 45.29% of users with Python3
# Memory Usage: 16.59 MB Beats 77.58% of users with Python3