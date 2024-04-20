class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        real_points = []
        for i in range(0, len(points)):
            real_points.append(points[i][0])
        real_points.sort()
        max = 0
        for i in range(1, len(points)):
            if max < real_points[i] - real_points[i - 1]:
                max = real_points[i] - real_points[i - 1]
        return max

# Runtime: 677 ms Beats 79.39% of users with Python3
# Memory Usage: 58.98 MB Beats 77.90% of users with Python3
