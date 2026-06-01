# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        curr = dummy
        while head:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr




        # if head is None or head.next is None:
        #     return head           
        # else:
        #     new_head = self.reverseList(head.next)
        #     head.next.next = head
        #     head.next = None
        #     return new_head




        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev
        