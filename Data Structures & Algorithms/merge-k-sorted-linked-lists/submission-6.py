# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand:
Given a list of k linked lists, return one list in sorted order where all linked lists are merged together
Input: List[ListNodes]: Output: ListNode
Constraints: Mantain the sorted order
Edge case: Emtpty lists, null linked list

Match:
Similar to merge 2 lists, we need to be comparing the values of the listNodes

Plan:
Have the first list as the main list:
For each linked list in lists: merge it with the main list


if not lists:
    return None
if len(lists) == 1:
    return lists[0]
first = lists[0]
for i in range(1, len(lists)):
    first = merge2Lists(first, lists[i])
return first

"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def merge2Lists(first, second):
            if not first:
                return second
            if not second:
                return first
            dummy = ListNode()
            tail = dummy
            while first and second:
                if first.val <= second.val:
                    temp = first.next
                    tail.next = first
                    first = temp
                else:
                    temp = second.next
                    tail.next = second
                    second = temp
                tail = tail.next
            if first:
                tail.next = first
            if second:
                tail.next = second
            return dummy.next



        first = lists[0]
        for i in range(1, len(lists)):
            first = merge2Lists(first, lists[i])
        return first
        
            
   

        