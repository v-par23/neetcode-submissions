class Union:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])

        return self.par[n]

    def union(self, node1, node2):
        r1, r2 = self.find(node1), self.find(node2)

        if r1 == r2:
            return
        elif self.rank[r1] > self.rank[r2]:
            self.rank[r1] += 1
            self.par[r2] = r1
        else:
            self.rank[r2] += 1
            self.par[r1] = r2
                    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = Union(n)

        for x,y in edges:
            u.union(x, y)
    
        return len([i for i in range(n) if i == u.par[i]]) 

        