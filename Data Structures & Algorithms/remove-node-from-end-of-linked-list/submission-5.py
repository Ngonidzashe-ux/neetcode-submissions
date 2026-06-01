# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Understand:
1. No edge cases, the solution has to handle everything

Plan:
2. Locate the n-1th node from the end of the list
3. Then remove it 

Implementation:
1. Create a dummy node and have it point to the head. This helps with single node lists i hope
2. Initialise first and second pointers pointing at the dummy node
3. Give second pointer a head start of n nodes
4. Then, shift the two pointers together until the second pointer is pointing to the last node
5. Then remove the next node to the first pointer

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy
        while n:
            second = second.next
            n-=1

        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next