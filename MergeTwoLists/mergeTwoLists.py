# *-* coding: utf-8 *-*


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp = ListNode(-1)
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            temp.next = l1
            l1.next = self.mergeTwoLists(l1.next, l2)
            return temp.next
        else:
            temp.next = l2
            l2.next = self.mergeTwoLists(l1, l2.next)
            return temp.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n3 = ListNode(3)
    n5 = ListNode(5)
    n7 = ListNode(7)
    n1.next = n3
    n3.next = n5
    n5.next = n7
    n7.next = None

    n2 = ListNode(2)
    n4 = ListNode(4)
    n6 = ListNode(6)
    n8 = ListNode(8)
    n2.next = n4
    n4.next = n6
    n6.next = n8
    n8.next = None

    s = Solution()
    res = s.mergeTwoLists(n1, n2)
    while res is not None:
        print(res.val)
        res = res.next
