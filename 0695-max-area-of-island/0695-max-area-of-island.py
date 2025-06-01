class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        maxa=0

        def dfs(r,c):
            if (r<0 or c<0 or r==len(grid) or c==len(grid[0]) or grid[r][c]==0 or ((r,c) in visited)):
                return 0
            visited.add((r,c))
            area=1
            area+=dfs(r+1,c)
            area+=dfs(r-1,c)
            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            return area
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 or (r,c) in visited:
                    continue
                maxa=max(dfs(r,c),maxa)
        
        return maxa
