"""
Plan:
1. Count the freq of each number
2. The most is len(nums)
3. Create a new array of len(nums)+1 where the index is freq
4. The entries are lists containing the numbers with that freq
5.Then starting at the end of the list, add each number to the res array until we have k elements
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for _ in range(len(nums)+1)]
        for num in count:
            freq[count[num]].append(num)
        print(freq)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if not k:
                    return res
                res.append(num)
                k -= 1
        return res


        
        
        