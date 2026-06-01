class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        array = [[] for i in range(len(nums) + 1)]
        for j in count:
            array[count[j]].append(j)
        for c in range(len(array)-1, 0, -1):
            for i in array[c]:
                result.append(i)
                if len(result) == k:
                    return result

        
            
        