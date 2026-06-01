"""
Understand:
Given rotated array, I need to return the minimum element in array
Constraints: nums all unique
Edge cases: nums = [], nums = all negative, nums = neg and pos

Match:
- This is similar to Binary Search because we need log n algo
- Similar to search for a specific element in a rotated array in that we have to consider multiple possilbe rotations

Plan:
- If nums[l] < nums[r], return nums[l] - no rotation
- Locate if we in the left or right subtree
- Left if mid > nums[l], then we have to look for smaller on the right
- Right otherwise and we have to look on the left
- Lets be updating res with our mid element

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        res = nums[0]
        l, r = 0, len(nums) - 1
        #no rotation
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[0]: #We are on the left portion
                l = mid + 1
            else:
                r = mid - 1
        return res

       

        