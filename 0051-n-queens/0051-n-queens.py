class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cset=set()
        dia1=set()
        dia2=set()
        res=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in cset or (r+c) in dia1 or (r-c) in dia2:
                    continue
                cset.add(c)
                dia1.add(r+c)
                dia2.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                cset.remove(c)
                dia1.remove(r+c)
                dia2.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
            