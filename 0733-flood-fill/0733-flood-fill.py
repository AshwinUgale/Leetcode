class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        ic=image[sr][sc]
        visited=set()
        def dfs(r,c):
            if (r>=rows or r<0 or
                c>=cols or c<0 or
                image[r][c]!=ic or
                (r,c) in visited):
                return
            visited.add((r,c))
            image[r][c]=color
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        dfs(sr,sc)
        return image