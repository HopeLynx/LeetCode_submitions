class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        m = 1
        while n:
            tmp = n % 10
            s += tmp
            m *= tmp
            n //=10
        return m-s

# Runtime: 20 ms, faster than 99.22% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 14.1 MB, less than 71.41% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
