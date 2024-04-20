class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if "++" in operation:
                x += 1
            else:
                x -= 1
        return x

# Runtime: 55 ms Beats 48.65% of users with Python3
# Memory Usage: 16.58 MB Beats 51.27% of users with Python3
