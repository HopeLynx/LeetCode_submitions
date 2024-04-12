class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

#Runtime:68 ms Beats 9.65% of users with Python3
#Memory Usage: 16.58 MB Beats 64.72% of users with Python3