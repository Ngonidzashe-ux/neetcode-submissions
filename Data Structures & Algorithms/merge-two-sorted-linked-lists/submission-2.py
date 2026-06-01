# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Understand:
1. Edge cases, if one or both lists are empty

Plan:
1. Create a dummy node and have a tail pointer tracking the last added node
NB. If neither is None
2. Compare the two nodes pointed at by the pointers
3. Add to the tail whichever is the smallest, should store the next node before doing this
4. Then move the pointer to the stored next
5. Move the tail to the next

Else:
    Just add the remaining list to the end of the newly merged list


"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = tail = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1.next
                tail.next = list1
                list1 = temp
            else:
                temp = list2.next
                tail.next = list2
                list2 = temp
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
            
            
