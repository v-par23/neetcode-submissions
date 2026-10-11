class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        inDigree = [0]*numCourses

        for src, dest in prerequisites:
            adj[src].append(dest)
            inDigree[dest] += 1
        
        queue = deque()
        for course in range(numCourses):
            if inDigree[course] == 0:
                queue.append(course)
        
        visited = 0
        while queue:
            curr = queue.popleft()
            visited += 1

            for nei in adj[curr]:
                inDigree[nei] -= 1
                if inDigree[nei] == 0:
                    queue.append(nei)
        
        if visited == numCourses:
            return True
        return False
         
