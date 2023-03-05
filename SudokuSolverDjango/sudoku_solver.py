class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        if self._solve(0, 0):
            return self.board
        else:
            return None

    def _solve(self, row, col):
        if row == 9:
            row = 0
            col += 1
            if col == 9:
                return True

        if self.board[row][col] != 0:
            return self._solve(row + 1, col)

        for val in range(1, 10):
            if self._is_valid(row, col, val):
                self.board[row][col] = val
                if self._solve(row + 1, col):
                    return True

        self.board[row][col] = 0
        return False

    def _is_valid(self, row, col, val):
        for i in range(9):
            if self.board[row][i] == val:
                return False

            if self.board[i][col] == val:
                return False

            if self.board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == val:
                return False

        return True

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = 0
