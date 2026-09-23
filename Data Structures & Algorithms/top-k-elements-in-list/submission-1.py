from collections import Counter 
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        countToValues = collections.defaultdict(list)
        for val, count in counter.items():
            countToValues[count].append(val)
        
        counts = [-count for count in countToValues.keys()] 
        heapq.heapify(counts)
        res = []
        for i in range(len(counts)):
            nextCount = -heapq.heappop(counts)
            for num in countToValues[nextCount]:
                if len(res) == k:
                    return res
                res.append(num)

        return res    
        