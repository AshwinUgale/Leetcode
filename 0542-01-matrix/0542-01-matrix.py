class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        res =  [[float('inf') for i in range(len(mat[0]))]  for j in range(len(mat))]
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] ==0:
                    res[i][j]=0
                    queue.append((i,j))
        
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            x,y=queue.popleft()
            for dx,dy in direction:
                nx = x+dx
                ny = y+dy
                if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
                    if res[nx][ny]>res[x][y]+1:
                        res[nx][ny]= res[x][y]+1
                        queue.append((nx,ny))
        return res


                