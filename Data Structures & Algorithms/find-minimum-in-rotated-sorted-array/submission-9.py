"""
Understand:

Return the minimum element from a rotated array.

Two types of arrays:
    1. Sorted Array
    2. Rotated Array

Sorted Array = leftMost element  less than the rightMostElement
Rotated Array = the opposite of sorted array
Need to determine the point of rotation using binary search:


Plan:
if length of nums == 0:
    return -1

#sorted
if nums[0] < nums[-1]:
    return nums[0]


#rotated
let result = max(nums)
let l = 0, r = len(nums) - 1

while l <= r:
    mid = (l + r) // 2

    #Still on the left side
    if nums[mid] > nums[0]:
        l = mid + 1
    else:
        r = mid - 1
        result = min(result, nums[mid])
return result


Plan:
    if length of nums is 0:
        return -1
    if nums is sorted:
        return nums[0]
    let l and r be left and right pointers
    let mid = mid index
    if nums[mid] which is the middle element is > than nums[0]:
        Then we are on the left side of the point of rotation
        Therefore, let l = mid + 1 so we search on the right
    else:
        Then we are on the right side of the point of rotation
        The current element might be the smallest but going to the left helps 
        r = mid - 1
        update the current result




"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        if nums[0] <= nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        result = max(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
                result = min(result, nums[mid])
        return result


        