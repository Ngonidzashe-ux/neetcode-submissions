"""

Understand:
You have a sliding window of length k and you should return an array that has the maximum element in the sliding window until you get to the end.



Plan:
if length of nums is 0: 
    return []
if k = 0:
    return []
if k > length of nums:
    return []
if k == 1: 
    return nums

output = []
determine the max in nums[:k]
add it to output
set it to be currentMax
Let l = 0 be the beginning of the sliding window
for r in range(k, len(nums)):
    newCandidate = nums[r]
    old candidate = nums[l]
    if newCandidate >= currentMax:
        currentMax = newCandidate
        output.append(currentMax)
    else if oldCandidate == currentMax:
        search for new candidate
    else if oldCandidate != currentMax:
        output.append(currentMax)
    else:








"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            num = -1 * nums[i]
            heapq.heappush(heap, (num, i))

        output = [-1*heap[0][0]]
        l = 0
        for r in range(k, len(nums)):
            newCandidate = -1 * nums[r]
            heapq.heappush(heap, (newCandidate, r) )
            l+=1
            while not l <= heap[0][1] <= r:
                heapq.heappop(heap)
            output.append(-1 * heap[0][0])
        return output

        