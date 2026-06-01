# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Two pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Get the length of the linked list
        N = 0
        cur = head
        while cur:
            N+=1
            cur = cur.next
        #Determine the number of the node to remove
        removeNode = N-n+1

        if removeNode == 1:
            return head.next
        

        cur = head
        for i in range(1, N):
            if (i+1) == removeNode:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
#Two Pointers
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
