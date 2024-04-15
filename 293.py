import re


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        a = [m.start() for m in re.finditer(digit, number)]
        tmp = []
        for item in a:
            tmp.append(int(number[:item] + number[item + 1:]))
        return str(max(tmp))

# Runtime: 35 ms Beats 61.24% of users with Python3
# Memory Usage: 16.48 MB Beats 89.75% of users with Python3
