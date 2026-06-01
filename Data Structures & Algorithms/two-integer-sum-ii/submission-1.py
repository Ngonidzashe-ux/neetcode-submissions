class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Brute Force Solution
        # for i in range(1, len(numbers)):
        #     num = target - numbers[i]
        #     for j in range(0, i):
        #         if numbers[j] == num:
        #             return [numbers[j],numbers[i]]


        #Optimal Solution
        l, r = 0, len(numbers)-1
        while l<r:
            if l<r and numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif l<r and numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1

        