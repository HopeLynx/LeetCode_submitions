class Solution:

    def minPartitions(self, n: str) -> int:
        ans = 0
        for i in n:
            if int(i) > ans:
                ans = int(i)
        return (ans)

# Runtime: 136 ms Beats 32.98% of users with Python3
# Memory Usage: 17.04 MB Beats 97.24% of users with Python3


