# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand:
Edge cases:
1. If None, return False

Plan:
1. Have a slow and fast pointer starting at the head:
2. While there is a fast.next, then we increment slow and fast
3. if at some point, fast and slow are pointing to the same node, then we return True
4. Otherwise return False

"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

    
        