class Solution:
    def check_rows(self, board):
        for row in board:
            elements = set()
            for elem in row:
                if elem != '.' and elem not in elements:
                    elements.add(elem)
                elif elem != '.' and elem in elements:
                    return False
            elements = set()
        return True
    
    def check_cols(self, board):
        cols = len(board[0])
        for col in range(cols):
            elements = set()
            for row in board:
                elem = row[col]
                if elem != '.' and elem not in elements:
                    elements.add(elem)
                elif elem != '.' and elem in elements:
                    return False
            elements = set()
        return True

    def check_grids(self, board):
        seen = set()
        for s in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (s // 3) * 3 + i
                    col = (s % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row for duplicates
        row_check = self.check_rows(board)

        # check col for duplicates
        col_check = self.check_cols(board)

        # check the 9 3 X 3 grids for duplicates
        grid_check = self.check_grids(board)

        return row_check & col_check & grid_check