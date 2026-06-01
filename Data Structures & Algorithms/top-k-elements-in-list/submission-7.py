

"""
Plan:
Count the occurences first and then create a max heap with the count and element and return the top K
"""
from collections import defaultdict, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if not k:
            return []
        count = Counter(nums)
        min_heap = []
        heapq.heapify(min_heap)


        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        results = []
        while min_heap:
            results.append(heapq.heappop(min_heap)[1])
        return results

            


        