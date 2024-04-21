class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"

        while start < end:
            while start < end and word[start] not in vowels:
                start += 1
            while start < end and word[end] not in vowels:
                end -= 1

            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1

        return "".join(word)

# Runtime: 49 ms Beats 63.57% of users with Python3
# Memory Usage: 17.52 MB Beats 51.57% of users with Python3