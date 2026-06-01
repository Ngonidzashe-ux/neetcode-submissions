# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand:
1. If not head or not head.next, then return head

Plan:
1. Find the number of nodes
2. Determine the first half
3. Reverse the last half
4. Merge the two lists starting with first half

"""
class Solution:
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list1, list2 = head, slow.next
        slow.next = None

        #Reverse list2
        prev, curr = None, list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        list2 = prev

        #merge
        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2




        