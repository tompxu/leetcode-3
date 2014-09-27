# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        else:
            p = head
            while p.next != None:
                if p.next.val == p.val:
                    temp = p.next
                    p.next = temp.next
                    del temp
                else:
                    p = p.next
                if p.next == None:
                    return head
            return head