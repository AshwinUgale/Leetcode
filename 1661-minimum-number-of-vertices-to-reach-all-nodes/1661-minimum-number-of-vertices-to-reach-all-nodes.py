class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n2].append(n1)
        res=[]
        for i in range(n):
            if not adj[i]:
                res.append(i)
        return res