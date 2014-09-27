# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        pre = ListNode(0)
        pre.next = head
        p = pre
        while True:
            if p.next == None or p.next.next == None:
                return pre.next
            elif p.next.val == p.next.next.val:
                q = p.next.next
                while q.next and q.next.val == p.next.val:
                    q = q.next
                p.next = q.next
            else:
                p = p.next