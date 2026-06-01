class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            #left sorted portion
            #if two cases are evaluating to the same thing, we can condense them by using or
            if nums[m] >= nums[l]:
                if target > nums[m]:
                    l = m+1
                elif target < nums[l]:
                    l = m+1
                else: 
                    r = m-1
            
            #right sorted portion
            else: 
                if target < nums[m]:
                    r = m-1
                elif target > nums[r]:
                    r = m-1
                else: 
                    l = m+1


        return -1

                    

