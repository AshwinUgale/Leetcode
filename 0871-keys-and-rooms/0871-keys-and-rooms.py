class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            print(visited)
            for r in rooms[n]:
                dfs(r)
            
        dfs(0)
        return len(visited)==len(rooms)
        