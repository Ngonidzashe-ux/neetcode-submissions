"""
Understand:
Given integers, return the k most frequent integers from the array
Input: List of integers and k
Output: Return a list of the k freq integers
Constraints: There is at least one integer in the array
Edge cases: Empty list, k is greater than the list and nums is just one number 

Match:
No Matching but this exploits counting of elements and the best way to do that is with a hashmap

Plan:
If not nums:
    return []
count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1

freq = [[] for i in range(len(nums) + 1)]
for num, cnt in count:
    freq[cnt].append(num)

res = []
for i in range(len(freq) - 1, -1, -1):
    for j in freq[i]:
        if k > 0:
            res.append(j)
            k -= 1
return res


"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for num in count:
            cnt = count[num]
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                if k > 0:
                    res.append(j)
                    k -= 1
        return res

        
        
        