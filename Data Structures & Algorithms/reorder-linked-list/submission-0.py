# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #This is to figure out the first and second halfs of the lists and slow will be pointed at the last node of the first half.
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        #The beginning of the second half but we need to reverse it
        second = slow.next
        slow.next = None
        prev = None

        #reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge two halfs
        first, second = head, prev #Because prev is gonna be pointing to the last element in the second half
        while second: #because second half of the list might be shorter
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


