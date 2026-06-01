class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) #initializing the indices of the nums array with the length of the longest increasing subsequence. Each length of an individual element is 1 at the beginning

        for i in range(len(nums)-1, -1, -1): #Lets start the iteration from the back of the list
            for j in range(i+1, len(nums)): #For each starting position i, we would want to evaluate the LIS of the elements that come after it.
                if nums[i]<nums[j]: #we need to check if the right element is greater than the left otherwise the right LIS wont matter.
                    LIS[i] = max(LIS[i], 1+LIS[j])
        
        return max(LIS)
        