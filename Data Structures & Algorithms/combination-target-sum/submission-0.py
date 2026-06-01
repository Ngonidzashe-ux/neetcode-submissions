class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] #to store the final result which is the combinations adding up to the target

        def dfs(i, cur, total): #mantain the i pointer, the current array and the total of the current array
            if total == target:
                res.append(cur.copy()) #We mantain a single variable list for current. We dont want to append current but the copy of the current so that we leave the original to be continuously used 
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
        

            
        

