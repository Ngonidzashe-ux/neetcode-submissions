"""
Understand:
- We come up with two arrays, prefix and postfix
- Prefix[i] is the product of the elements on the left of i
- Postfix[i] is the product of the elements on the right of i
- So the output[i] will be the product of prefix[i] and postfix[i]


"""



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1] #multiply the prefix of the previous number with the previous number to get current prefix

        postfix = [1] * n
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        output = [1] * n
        for i in range(n):
            output[i] = prefix[i] * postfix[i]
        
        return output

        