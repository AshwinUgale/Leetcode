class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n ==1:
            return True
        adj=defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited=set()
        print(adj)
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)
            