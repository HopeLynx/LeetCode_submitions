class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        diction = {}
        for item in nums:
            if item in diction:
                diction[item] += 1
            else:
                diction[item] = 1
            a = []
        for i in range(len(diction)):
            min_value = min(diction.values())
            tmp = {key: value for key, value in diction.items() if value == min_value}
            tmp_key = max(tmp.keys())
            print(tmp)
            a.extend(([tmp_key] * min_value))
            del diction[tmp_key]
        return a

# Runtime: 60 ms Beats 7.56% of users with Python3
# Memory Usage: 16.60 MB Beats 56.91% of users with Python3
