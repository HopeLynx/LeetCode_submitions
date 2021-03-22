class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        x = list()
        for i in range(0,len(candies)):
            if (max_c <= candies[i]+extraCandies):
                x.append(True)
            else: 
                x.append(False)
        return x
#Runtime: 40 ms, faster than 57.65% of Python3 online submissions for Kids With the Greatest Number of Candies.
#Memory Usage: 14.3 MB, less than 56.68% of Python3 online submissions for Kids With the Greatest Number of Candies.
