# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        else:
            start = ListNode(0)
            start.next = head
            i = start
            while i.next and i.next.next:
                temp = i.next.next
                i.next.next = temp.next 
                temp.next = i.next
                i.next = temp
                i = i.next.next
            return start.next