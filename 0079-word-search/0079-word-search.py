class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r>=rows or c>=cols or
                word[i]!=board[r][c] or
                (r,c) in visited):
                return False
            visited.add((r,c))
            result = (backtrack(r,c+1,i+1) or
                      backtrack(r+1,c,i+1) or
                      backtrack(r-1,c,i+1)or 
                      backtrack(r,c-1,i+1))
            visited.remove((r,c))
            return result

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0): return True
        return False

        