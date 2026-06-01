class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # numMap = {}
        # for num in nums:
        #     numMap[num] = numMap.get(num, 0) + 1
        # for i in range(len(nums)):
        #     l, r = i, (len(nums) - 1)
        #     while l < r:
        #         twoSum = nums[l] + nums[r]
        #         numMap[nums[l]]-=1
        #         numMap[nums[r]]-=1
        #         target = 0 - twoSum
        #         if target in numMap and numMap[target] != 0:
        #             ans = sorted([nums[l], nums[r], target])
        #             if ans not in res:
        #                 res.append(ans)
        #         numMap[nums[l]]+=1
        #         numMap[nums[r]]+=1
        #         r -=1

        # return res
        
        res = []
        nums.sort()
        for i, curNum in enumerate(nums):
            #If the number is positive, the right nums are positive too and cant sum to 0 so just break
            if curNum > 0:
                break
            
            #Check for duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #Check for the twoSum that adds up to Threesum with this one
            l, r = i+1, (len(nums)-1)
            while l < r:
                threeSum = curNum + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([curNum, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    while nums[r] == nums[r+1] and l < r:
                        r-=1
        return res



                
