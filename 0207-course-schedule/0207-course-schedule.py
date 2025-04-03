class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = { i:[] for i in range(numCourses)}
        for cor,pre in prerequisites:
            edges[cor].append(pre)
        print(edges)
        visited = set()
        def dfs(n):
            if n in visited:
                return False
            if edges[n] == []:
                return True
            visited.add(n)
            for pre in edges[n]:
                if not dfs(pre):
                    return False
            visited.remove(n)
            edges[n] = []
            return True


        for n in range(numCourses):
            if not dfs(n): return False
        return True
