class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2

# Runtime: 28 ms Beats 96.65% of users with Python3
# Memory Usage: 16.54 MB Beats 73.91% of users with Python3
