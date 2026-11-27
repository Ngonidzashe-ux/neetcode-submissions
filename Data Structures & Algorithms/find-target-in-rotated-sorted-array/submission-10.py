"""
Understand:

We have two sorted arrays, left and right.
The midpoint can either be on the left or right array.
If the midpoint is in the left array:
    If target > midpoint element:
        we search on the right
    if target < midpoint element:
        can be on the left or right
        have to determine if target is in left array
        if nums[l] <= target:
            we search left
        else:
            go right
Plan:



"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            #Mid in left array
            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    if nums[l] <= target:
                        r = mid -1
                    else:
                        l = mid + 1

            else:
                if target > nums[mid]:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1

                else:
                    r = mid - 1
        return -1

        