"""
Understand:
Given weights of stones, extract the two heaviest, and the difference is inserted back into the array until we have one left
Input: stones, List[int] and Output = Weight of remaining stone or 0 if there is none

Match:
Plan:
if not stones:
    return 0
stones = [(-1 * i) for i in stones]
heap = heapq.heapify(stones)
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    rem = a - b
    if rem != 0:
        heapq.heappush(rem)
return (-1 * heap[0]) if len(heap) != 0 else 0





"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heap = [(-1 * i) for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            rem = a - b
            if rem != 0:
                heapq.heappush(heap, rem)
        return (-1 * heap[0]) if len(heap) != 0 else 0
        