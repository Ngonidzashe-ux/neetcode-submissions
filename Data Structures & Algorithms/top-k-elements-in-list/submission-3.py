class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First thing is to count in a hashmap
        counter = 0
        count = {}
        res = [ [] for _ in range(len(nums) + 1)]
        output = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i in count:
            res[count[i]].append(i)

        for i in range(len(res)-1, -1, -1):
            for j in res[i]:
                output.append(j)
                counter+=1
                if counter == k:
                    return output

        


        

        
      