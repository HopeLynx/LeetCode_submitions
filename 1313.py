class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(0,len(nums),2):
            a += [nums[i+1]]*nums[i]
        return a
# Runtime: 60 ms, faster than 93.03% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14.6 MB, less than 95.40% of Python3 online submissions for Decompress Run-Length Encoded List.
