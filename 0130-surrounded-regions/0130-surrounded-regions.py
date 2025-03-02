class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        # unSur = set()

        def countS(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or board[r][c]!="O") :
                return 
            # unSur.add((r,c))
            board[r][c] = "T"
            countS(r+1,c)
            countS(r-1,c)
            countS(r,c+1)
            countS(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0,ROWS-1] or c in  [0,COLS-1])):
                    countS(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" :
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

            