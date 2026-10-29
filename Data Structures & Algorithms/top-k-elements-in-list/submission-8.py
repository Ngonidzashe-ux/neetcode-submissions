"""
Understand: 
Count the occurence of each element and then return the top k occuring elements
return a list

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        for num in nums:
            freqCount[num] = freqCount.get(num, 0) + 1

        result = [[] for i in range(len(nums) + 1)] 
        for key in freqCount:
            result[freqCount[key]].append(key)
        output = []
        for i in range(len(result) - 1, -1, -1):
            for j in result[i]:
                if k > 0:
                    output.append(j)
                    k-=1
                else:
                    return output
        return output
                
        