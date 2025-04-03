class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = { i:[] for i in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i!=j:
                    if isConnected[i][j]==1:
                        edges[i].append(j)
        print(edges)
        print(edges[0])
        component=0
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in edges[node]:
                dfs(nei)
        
        for n in range(len(isConnected)):
            print(visited)
            if n in visited:
                continue
            else:
              
                component+=1
                dfs(n)
        return component