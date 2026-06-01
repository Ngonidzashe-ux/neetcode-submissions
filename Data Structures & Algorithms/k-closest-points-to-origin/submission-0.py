class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -1 * math.sqrt((x**2) + (y**2))
            point = (dist, (x, y))
            heapq.heappush(heap, point)
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for dist, coord in heap:
            res.append(list(coord))
        return res



