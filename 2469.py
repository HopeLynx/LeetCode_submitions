class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

# Runtime: 25 ms Beats 96.95% of users with Python3
# Memory Usage: 16.53 MB Beats 42.64% of users with Python3