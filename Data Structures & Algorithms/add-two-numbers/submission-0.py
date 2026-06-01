# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand:
Given 2 linked lists of digits representing numbers in reverse order, find their sum and return the resulting linked list sum in reverse too
Input: 2 Linked Lists: Output: One Linked List
Constraints: One digit per node
Edge cases. Empty linked lists, one empty one not, having a carry

Match: Like merge2Lists, there is need of tracking nodes from the two lists concurrently
Like reverseList, it might be needed to reverse these lists

Plan:
Reverse the list, extract the digits into a number, add the numbers, create a linked list of the sum, then reverse it
Reverse the list, add the numbers in place handling the carry passing it on to the next, then creating a new node if need and then reverse it

"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l2 or l1 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            digit = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            tail.next = ListNode(digit)

            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
         










                
        

        

        
