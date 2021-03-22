class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
#Runtime: 24 ms, faster than 94.40% of Python3 online submissions for Defanging an IP Address.
#Memory Usage: 14.2 MB, less than 37.14% of Python3 online submissions for Defanging an IP Address.
