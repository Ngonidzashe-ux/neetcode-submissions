"""
Understand:
- If we are given an unrotated array, i.e. nums[0] < nums[len(nums) -1 ], return the first element
- Need to determine which side to search
- Thus find the middle element
- If middle element is greater than the leftmost, then we are in left subarray, then we have to search for the minimum at the right
- if middle element is less than leftmost, then the min is either that element or the element on the left


Plan:
- If len(nums) is 1, return the single element
- If array is not rotated i.e. nums[0] < nums[last], return nums[0]
- Else:
    - find mid index and element: l + r //2
    - While l < r:
    - If nums[l] < mid, then mid is in the left, so we update l = mid + 1
    - If nums[l] == mid: retun it
    - If nums[l] > mid, then we are on the right, we just need to update our right pointer to scoop to the left
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

        