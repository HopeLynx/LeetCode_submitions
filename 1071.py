from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            first = gcd(len(str1),len(str2))
            return str1[:first]
        else:
            return ""


# Runtime: 33 ms Beats 78.62% of users with Python3
# Memory Usage: 16.55 MB Beats 68.54% of users with Python3