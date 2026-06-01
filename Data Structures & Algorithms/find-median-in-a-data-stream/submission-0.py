class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        #if the large heap exists already and the num you want to add is greater that the min of the large heap, then add the num to the large heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        #However, if the large heap does not exist yet or the num you wanna add is smaller than the min of the large heap, then by default, just add it to the small heap

        else:
            #push the -ve version of num into the small heap
            heapq.heappush(self.small, -1 * num)

#if the difference between the two heaps is more than 1 where the small heap is longer than the larger heap,
#We have to pop the max from the small heap, multipy by one to get the original value and then push that value into the larger heap.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
#if its the larger heap that is too long, then we pop the min from it and push it into the small heap and we multiply it by -1 so that its a max heap
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        #if the small heap is greater than the larger one, then just return the max of the small one
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        #otherwise return the min of the larger one
        elif len(self.large) > len(self.small):
            return self.large[0]
        #if the lengths are the same, then take the max of small and min of large, then take the average
        return (-1 * self.small[0] + self.large[0]) / 2.0
