# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverseList(self, ...): Defines a method named reverseList which is a part of a class (indicated by the presence of self).
# self: Refers to the instance of the class. This is a conventional name for the first parameter of instance methods in Python.
# head: Optional[ListNode]: Indicates that the head parameter is expected to be of type Optional[ListNode]. Optional is used from the typing module and means that head can either be of type ListNode or None.
# -> Optional[ListNode]: Specifies that the method returns a value of type Optional[ListNode], meaning the return value can either be of type ListNode or None.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
        