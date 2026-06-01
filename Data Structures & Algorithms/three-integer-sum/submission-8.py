"""
Understand:
Given a nums array, return a list with a list of the triplets that sum up to 0
Constraints: No duplicates are allowed
Edge cases: Empty array, one element, all negative, same element throughout

Match:
Like contains duplicate, we need to ensure there is no duplication in our results
Like 2sum, where we find 2 numbers summing up to the target, we have to do something similar with 3 numbers and 0 as the target
To avoid duplicates, we need to sort the numbers 
Plan:

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        mySet = set() #to track duplicates
        res = []
        for i in range(len(nums)):

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j],  nums[k]) not in mySet:
                        res.append([nums[i], nums[j],  nums[k]])
                        mySet.add((nums[i], nums[j],  nums[k]))
                    j += 1
                    k -= 1
                   
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res
            

                



        