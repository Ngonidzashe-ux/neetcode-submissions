class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans1 = 0
        ans2 = 0
        for i in nums:
            ans1 = ans1 ^ i
        for j in range(n+1):
            ans2 = ans2 ^ j
        return ans2 ^ ans1


        #Simpler approach of taking the sum of the range and the nums and subtracting them
        #This can be done in one loop.
        # res = len(nums)
        # for i in range(len(nums)):
        #     res += (i-nums[i])
        # return res

        