class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        last = None
        for i in flowerbed:
            if i == 0:
                if not last:
                    cnt += 1
                    last = True
                else:
                    last = False
            else:
                if last != None and last == True:
                    cnt -= 1
                last = True
        print(cnt)
        return cnt >= n

# Runtime: 119 ms Beats 97.44% of users with Python3
# Memory Usage: 16.38 MB Beats 72.60% of users with Python3