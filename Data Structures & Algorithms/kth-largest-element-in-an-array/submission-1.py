class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # #O(nlogn)
        # heap = []
        # for i in nums:
        #     heapq.heappush(heap, i)
        # for i in range (len(nums) - k):
        #     heapq.heappop(heap)
        # return heapq.heappop(heap)
        
        #O(klogk) - best way if they ask to explain in interview
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap,num)
        return heap[0]



