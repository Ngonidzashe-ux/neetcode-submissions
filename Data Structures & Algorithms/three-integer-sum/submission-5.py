"""
Understand:
- Sort the numbers so that its easier for us to identify the duplicates
- Then have a for loop, which will start at each number
- For each pointed number, we search for the additional two numbers on its right using  a while loop and two pointers
- Add the numbers to a res set
- Move on to the next number in the for loop.
- Check if its equal to the previous pointed number, contiue if true
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    res.add((nums[j], nums[k], nums[i]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] +  nums[i] < 0:
                    j += 1
                else:
                    k -= 1
        output = list(res)
        for i in range(len(output)):
            output[i] = list(output[i])
        return output

        