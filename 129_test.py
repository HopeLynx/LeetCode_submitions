# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(node, cntr, s):
    if node:
        s += str(node.val)
        if not node.left and not node.right:
            cntr += int(s)
        else:
            cntr += int(pre_order(node.left, 0, s))
            cntr += int(pre_order(node.right, 0, s))
    return cntr


def sumNumbers(root):
    return pre_order(root, 0, "")


def main():
    node1 = TreeNode(2, )
    node2 = TreeNode(3, )
    root = TreeNode(1, node1, node2)
    print(sumNumbers(root))


if __name__ == "__main__":
    main()
