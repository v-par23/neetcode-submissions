class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
     
        # 1. Standard graph build from LeetCode input
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))
            
        # --- STANDARD DIJKSTRA TEMPLATE BEGINS HERE ---
        minHeap = []
        dist = [sys.maxsize] * n
        stops = [sys.maxsize] * n
        
        dist[src] = 0
        stops[src] = 0
        heapq.heappush(minHeap, (0, src, 0)) # (curDist, curNode)
        
        while minHeap:
            curDist, curNode, curStop = heapq.heappop(minHeap)
            
            if curNode == dst:
                return curDist
            
            if curStop == k + 1:
                continue 

            for nextNode, nextWeight in adj[curNode]:
                nextDist = curDist + nextWeight
                nextStop = curStop + 1
                
                if nextDist < dist[nextNode]:
                    dist[nextNode] = nextDist
                    stops[nextNode] = nextStop
                    heapq.heappush(minHeap, (nextDist, nextNode, nextStop))
                    
                elif nextStop < stops[nextNode]:
                    stops[nextNode] = nextStop
                    heapq.heappush(minHeap, (nextDist, nextNode, nextStop))
        return -1
