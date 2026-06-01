"""
Understand:
Understand: Find index of target in rotated sorted array
 (unique integers, sorted ascending). Input: List[int], 
 target: int, Output: int. Edge cases: empty array, 
 single element, target not present, all negative. 
 Constraints: O(log n) time.”

Match: Like Find Minimum in Rotated Sorted Array (binary search 
for pivot). Uses binary search to exploit sorted halves, 
similar to standard Binary Search.

Plan: 1. If empty, return -1. 2. Binary search: if nums[mid] == target, return mid. If nums[mid] > nums[l], left half is sorted; check if target in [nums[l], nums[mid]). Else, right half is sorted; check [nums[mid], nums[r]]. 3. Return -1 if not found.



"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, (len(nums) - 1)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: #We are on the LHS
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                

            else:                 #We are on the RHS
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        