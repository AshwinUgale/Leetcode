class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        arr=[]
        def dfs(n):
            arr.append(n)
            if n == len(graph)-1:
                res.append(arr.copy())
            else: 
                for nei in graph[n]:
                    dfs(nei)
            arr.pop()
        dfs(0)
        return res
            
            