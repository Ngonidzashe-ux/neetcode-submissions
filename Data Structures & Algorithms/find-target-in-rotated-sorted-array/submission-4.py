"""
Understand: 
- Return the index of target num from rotated sorted array
- Does the array contain negative nums: Yes

Match:
- This seems like a binary search algorithm since it runs in log n and it is similar to Find Minimum in rotated array

Plan:
- Initialise l, r = 0, len(nums) - 1
- While l < r
    - Calculate the mid index and find the mid number
    - Check if mid is the number, return index if true
    - If we are on the RHS:
        - If target > nums[r]:
            - Check the left side
        - else
            - Check the RHS
    
    -Else:
        - If target > nums[l]:
            - Check on the LHS
        - Else
            - Check on the right


"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: #On the LHS
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            else:
                if nums[mid] < target <= nums[r] :
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 

        