"""
Understand:
Return the minimum number of tasks that allow each identical task to be processed seperately.

Match:
Plan:
if not tasks:
    return 0
- We have a max of 26 distinct characters
- We are going to count the freq of all characters though using hashmap that is O(n) TIME
- We want to have a time variable that tracks time
- We want to have a max heap that is going to give us a max in log n time
- Then a q that is going to be storing the remaining freq to process and the earliest time to be processed
- Dont put zeros


"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        count = Counter(tasks)
        print(count)
        heap = [-cnt for cnt in count.values()]
        time = 0
 
        heapq.heapify(heap)
        q = deque()
        while heap or q:
            time += 1
            if heap:
                val = heapq.heappop(heap)
                val += 1
                if val:
                    q.append((val, time+n))

            if q and q[0][1] <= time:
                heapq.heappush(heap, q.popleft()[0])
        return time                

            




