class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for i in range(len(rooms)):
            for j in rooms[i]:
                adj[i].append(j)
        visited=set()
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            print(visited)
            for r in adj[n]:
                dfs(r)
            
        dfs(0)
        return len(visited)==len(rooms)
        