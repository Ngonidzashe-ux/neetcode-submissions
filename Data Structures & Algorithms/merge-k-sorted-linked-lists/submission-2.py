# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand:
- Merge k linked lists into a single sorted list
- Input = list of k linked lists, output = single linked list
- Edge cases: Negative values in the linked lists, empty list


Match:
- This is similar to merge 2 lists(2 pointer technique) and we can extend this by having a standalone function that merges 2 linked lists.

Plan:
-If list is Empty,return None
-def merge2Lists
- list1, list2 = list[0], None
- for i in lists[1:]
    - list2 = lists[i]
    -temp = merge2lists(list1, list2)
    -list1 = temp
return temp

"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        def merge2Lists(list1, list2):
            if not list1 and not list2:
                return None
            if not list1:
                return list2
            if not list2:
                return list1
            tail = dummyNode = ListNode(0)
            while list1 and list2:
                if list1.val <= list2.val:
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
            return dummyNode.next


        list1, list2 = lists[0], None
        for i in lists[1:]:
            list2 = i
            temp = merge2Lists(list1, list2)
            list1 = temp
        return temp


        