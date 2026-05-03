class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        downs = []
        for i in range(9):
            downs.append({})
        
        squares = []
        for i in range(9):
            squares.append({})

        for i in range(9):
            row={}
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row:
                    return False
                row[board[i][j]] = True

                if board[i][j] in downs[j]:
                    return False
                downs[j][board[i][j]] = True

                if board[i][j] in squares[i//3*3+j//3]:
                    return False
                squares[i//3*3+j//3][board[i][j]] = True
        return True