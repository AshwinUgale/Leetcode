class Solution:
    def totalNQueens(self, n: int) -> int:
        cset=set()
        dia1=set()
        dia2=set()
        count=0
        def backtrack(r): 
            if r==n:
                nonlocal count
                count+=1
                return
            for c in range(n):
                if c in cset or (r+c) in dia2 or (r-c) in dia1:
                    continue
                cset.add(c)
                dia1.add(r-c)
                dia2.add(r+c)
                backtrack(r+1)
                cset.remove(c)
                dia1.remove(r-c)
                dia2.remove(r+c)

        backtrack(0)
        return count
