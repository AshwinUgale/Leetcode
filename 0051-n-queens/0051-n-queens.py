class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cset=set()
        pdia=set()
        ndia=set()
        res = []
        board=[["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cset or (r+c) in pdia or (r-c) in ndia:
                    continue
                cset.add(c)
                pdia.add(r+c)
                ndia.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                cset.remove(c)
                pdia.remove(r+c)
                ndia.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res