from typing import List
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
       
        maxHeap = []
        for count in taskCount.values():
            maxHeap.append(-count)
        heapq.heapify(maxHeap)

        time = 0
        wait_queue = deque()

        while maxHeap or wait_queue:
            time += 1

            if maxHeap:
                currentTask = heapq.heappop(maxHeap)
                currentTask += 1

                if currentTask != 0:
                    wait_queue.append((currentTask, time + n))
                
            if wait_queue and wait_queue[0][1] == time:
                heapq.heappush(maxHeap, wait_queue.popleft()[0])
        
        return time


