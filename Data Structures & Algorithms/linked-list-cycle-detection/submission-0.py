# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ##This is my own code and approach
        # visited=[]
        # while head != None:
        #     if head.val in visited:
        #         return True
        #     visited.append(head.val)
        #     head = head.next
        # return False
        slow, fast = head, head
        while fast and fast.next: #This is enough to check for Null as fast will always reach the end of the loop first if it exists. We check fast and fast.next because fast is shifted by 2 so the only way to check the one skipped is to check it as fast.next before the skipping takes place
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #Check for cycle
                return True
        return False
            
        

        