class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        x = []
        for i in range(0,len(candies)):
            if (max_c <= candies[i]+extraCandies):
                x.append(True)
            else: 
                x.append(False)
        return x
#Runtime: 34 ms, faster than 90.49% of Python3 online submissions for Kids With the Greatest Number of Candies.
#Memory Usage: 16.48 MB, less than 90.98% of Python3 online submissions for Kids With the Greatest Number of Candies.
