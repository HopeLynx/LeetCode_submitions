class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        minim = 10000000
        for i in range(0, len(cards)):
            if cards[i] in dic:
                if i - dic[cards[i]] + 1 < minim:
                    minim = i - dic[cards[i]] + 1
            dic[cards[i]] = i
        if minim == 10000000:
            return -1
        else:
            return minim

# Runtime: 584 ms Beats 98.69% of users with Python3
# Memory Usage: 35.76 MB Beats 69.90% of users with Python3