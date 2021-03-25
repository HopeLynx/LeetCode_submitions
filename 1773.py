class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        tmp = ["type", "color", "name"].index(ruleKey)
        ans = 0
        for i in range(len(items)):
            if (items[i][tmp]==ruleValue):
                ans += 1
        return ans
            
# Runtime: 232 ms, faster than 94.20% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.7 MB, less than 21.67% of Python3 online submissions for Count Items Matching a Rule.
