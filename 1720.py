class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
#         xor(a,b) = a^b
        for i in range(len(encoded)):
            ans.append(ans[i]^encoded.pop(0))
        return ans
      
# Runtime: 288 ms, faster than 6.67% of Python3 online submissions for Decode XORed Array.
# Memory Usage: 15.5 MB, less than 99.66% of Python3 online submissions for Decode XORed Array.
