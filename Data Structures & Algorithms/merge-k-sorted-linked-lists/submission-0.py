# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Edge case if the lists is Null or length 0 to return None
        if not lists or len(lists) == 0:
            return None

#We are going to be taking pairs of linked lists and merging them until there is only one linked list remaining
#We are gonna keep merging as long as the length of the lists > 1
        while len(lists) > 1:
            #store the lists in the mergedLists
            mergedLists = []
            #Iterate through lists and our increment is gonna be 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                #l2 might be out of bounds if we have an odd number
                #If i+1 is in bounds, good else return None for the l2
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                #Then you are gonna append merge l1 and l2 together and append to the  mergedLists 
                mergedLists.append(self.mergeList(l1, l2))
            #update the lists to be mergedlists
            lists = mergedLists
        #Return the final merged linked list
        return lists[0]
        
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next   
