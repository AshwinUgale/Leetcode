class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjL=defaultdict(list)
        for n1,n2 in edges:
            adjL[n1].append(n2)
            adjL[n2].append(n1)
        # visited = set()
        # def dfs(n):
        #     if n == destination:
        #         return True
        #     visited.add(n)
        #     for nei in adjL[n]:
        #         if nei not in visited:
        #             if dfs(nei):
        #                 return True
        #     return False
        # return dfs(source)
        
        
        
        #DFS
        q = deque([source])
        visited = set()
        def bfs():
            while q:
                val=q.popleft()
                if val == destination:
                    return True
                if val in visited:
                    continue
                visited.add(val)
                for nei in adjL[val]:
                    if nei not in visited:
                        q.append(nei)
            return False
        return bfs()
            