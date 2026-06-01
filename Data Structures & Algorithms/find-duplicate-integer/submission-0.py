"""
Problem is a linked list.
n + 1 integers means the largest index in nums = n
nums are in range [1, n] means we can access any index position except 0
So we can look this think as a linked list where each value in nums point to an index position with the next pointer etc
We are guarrantedd a cycle and also a portion outside a cycle.
So use slow and fast pointer to find where they meet.
Both start at 1. so slow = nums[slow], fast = nums[nums[fast]]
Then when they meet, there is an algorithm that says the distance between that point and the start of the cylcle is the same as the distnace between teh start of the cycle and the beginning of the linked list. so we introduce a new pointer that starts at the beginning of array and traverses at same speed as slow until they meet. Thats the beginning of cycle and return the number.
We are basically looking for the start of the cycle. the one with multiple arrows coming into it and leaving from it

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        