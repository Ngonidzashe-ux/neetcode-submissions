class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [min(nums)] * (n)
        dp_min = [max(nums)] * (n)
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp_max[i] = dp_min[i] = nums[i]
            else:
                dp_max[i] = max(nums[i], nums[i]*dp_max[i+1], nums[i]*dp_min[i+1] )
                dp_min[i] = min(nums[i], nums[i]*dp_max[i+1], nums[i]*dp_min[i+1] )
        print(dp_max)
        print(dp_min)

        return max(dp_max)


        