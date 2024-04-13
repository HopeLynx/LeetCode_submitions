class Solution:
    def trap(self, height: List[int]) -> int:
        lh = len(height)
        left = [0] * lh
        right = [0] * lh
        trapped_water = 0
        if lh < 3:
            return 0
        left[0] = height[0]
        right[lh - 1] = height[lh - 1]
        for i in range(1, lh):
            left[i] = max(height[i], left[i - 1])
        for i in range(lh - 1 - 1, -1, -1):
            right[i] = max(height[i], right[i + 1])
        print(left, right)
        for i in range(0, lh):
            trapped_water += (min(left[i], right[i]) - height[i])
        print(trapped_water)
        return trapped_water

# Daily task
# Runtime: 107 ms Beats 42.11% of users with Python3
# Memory Usage: 18.88 MB Beats 7.16% of users with Python3
