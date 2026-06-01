# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy 
        cur1, cur2 = list1, list2
        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.val < cur2.val:
                    current.next = cur1
                    current = current.next
                    cur1 = cur1.next
                     
                else:
                    current.next = cur2
                    current = current.next
                    cur2 = cur2.next
            elif cur1:
                current.next = cur1
                break
            else:
                current.next = cur2
                break
        return dummy.next
        



            