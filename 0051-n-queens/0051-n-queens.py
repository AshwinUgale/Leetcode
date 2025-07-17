class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet=set()
        pdiag=set()
        ndiag=set()
        board=[['.' for i in range(n)] for i in range(n)]
        res=[]
        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if (c in colSet or (r-c) in ndiag or
                    (r+c) in pdiag ):
                    continue
                board[r][c]="Q"
                colSet.add(c)
                ndiag.add(r-c)
                pdiag.add(r+c)
                backtrack(r+1)
                board[r][c]="."
                colSet.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
        backtrack(0)
        
        return res
            