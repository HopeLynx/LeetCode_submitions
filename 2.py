# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def add_to_end(head: ListNode, val: Any) -> None:
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = ListNode(val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l11 = []
        n = l1
        while n is not None:
            l11.append(n.val)
            n = n.next
        l22 = []
        n = l2
        while n is not None:
            l22.append(n.val)
            n = n.next

        ll1 = len(l11)
        ll2 = len(l22)
        tmp = 0
        s1 = 0
        s2 = 0
        for i in range(ll1 - 1, 0 - 1, -1):
            s1 += l11[i] * 10 ** (ll1 - tmp - 1)
            tmp += 1
        tmp = 0
        for i in range(ll2 - 1, 0 - 1, -1):
            s2 += l22[i] * 10 ** (ll2 - tmp - 1)
            tmp += 1
        s = (s1 + s2)
        f = ListNode(s % 10)
        s //= 10
        if s:
            tmp = len(str(s))
            for i in range(tmp):
                add_to_end(f, s % 10)
                s //= 10
        return f

# Runtime: 68 ms Beats 5.52% of users with Python3
# Memory Usage: 16.64 MB Beats 48.68% of users with Python3
