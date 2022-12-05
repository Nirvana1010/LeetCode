class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        def dfs(column, diagonal_lr, diagonal_rl, i, board):
            if i == n:
                boards.append(board[:])
                return
            
            for j in range(n):
                if j in column or (j + i) in diagonal_rl or (i - j) in diagonal_lr:
                    continue
                row = ['.'] * n
                row[j] = 'Q'
                row = ''.join(row)
                board.append(row)
                dfs(column+[j], diagonal_lr+[i-j], diagonal_rl+[i+j], i+1, board)
                board.pop()
        
        dfs([], [], [], 0, [])
        return boards