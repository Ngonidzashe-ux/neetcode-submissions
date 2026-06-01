# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Understand: If head is None, return None
Plan:
- Have new pointers, curr and prev pointers
- For curr node, store the next node in a temp variable
- Then let curr pointer point to prev.
- Shift the prev node to curr
- Shift curr to temp

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
