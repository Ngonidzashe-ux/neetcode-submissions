class Solution:
    def findMin(self, nums: List[int]) -> int:
        #If we are dealing with minimum, you cant initialize your result variable to zero. You have to initialize to one of the elements in the array.
        res = nums[0] 
        left, right = 0, (len(nums)-1)
        while left <= right:
            #if sorted already, return the left element as smallest
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            #If not sorted, calculate middle point and potentially record that as our result if smaller than existing
            m = (left+right)//2
            res = min(res, nums[m])

            #Check the portion you are in
            if nums[m] >= nums[left]: #You  are in the left and need to move to right
                left = m+1
            else:
                right = m-1
        return res

