class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_mat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                above = self.prefix_mat[r][c + 1]
                prefix += matrix[r][c]
                self.prefix_mat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2 + 1
        col2 = col2 + 1

        bottom_area = self.prefix_mat[row2][col2]
        left_area = self.prefix_mat[row2][col1 - 1]
        above_area = self.prefix_mat[row1 - 1][col2]
        additive_area = self.prefix_mat[row1 - 1][col1 - 1]

        res = bottom_area - above_area - left_area + additive_area
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)