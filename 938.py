# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if (root != None):
            ans  = self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) 
            if (low <= root.val <= high):
                return ans + root.val
            else:
                return ans
        else: 
            return 0
            
# Runtime: 280 ms, faster than 16.14% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.3 MB, less than 59.32% of Python3 online submissions for Range Sum of BST.

# TODO resolve
