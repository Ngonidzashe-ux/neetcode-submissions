class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        numMap = {}
        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
        for i in range(len(nums)):
            l, r = i, (len(nums) - 1)
            while l < r:
                twoSum = nums[l] + nums[r]
                numMap[nums[l]]-=1
                numMap[nums[r]]-=1
                target = 0 - twoSum
                if target in numMap and numMap[target] != 0:
                    ans = sorted([nums[l], nums[r], target])
                    if ans not in res:
                        res.append(ans)
                numMap[nums[l]]+=1
                numMap[nums[r]]+=1
                r -=1

        return res
                
