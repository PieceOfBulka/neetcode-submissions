class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0]*9
        col = [0]*9
        square = [0]*9

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                val = int(board[i][j])

                if (1 << val) & row[i]:
                    return False
                
                if (1 << val) & col[j]:
                    return False

                if (1 << val) & square[i//3*3 + j//3]:
                    return False

                row[i] |= (1<<val)
                col[j] |= (1<<val)
                square[i//3*3 + j//3] |= (1<<val)
        
        return True