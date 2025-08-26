from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
    
        def backtrack(row, cols, pos_diagonals, neg_diagonals, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
                    continue
                
                # Make the move
                board[row][col] = 'Q'
                cols.add(col)
                pos_diagonals.add(row + col)
                neg_diagonals.add(row - col)
                
                # Go to the next row
                backtrack(row + 1, cols, pos_diagonals, neg_diagonals, board)
                
                # Undo the move (backtrack)
                board[row][col] = '.'
                cols.remove(col)
                pos_diagonals.remove(row + col)
                neg_diagonals.remove(row - col)
        
        # Initialize board
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return res