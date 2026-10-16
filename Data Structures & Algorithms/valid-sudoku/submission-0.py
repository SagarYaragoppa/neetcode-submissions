class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    if x in seen:
                        return False
                    seen.add(x)

        # Check columns
        for j in range(9):
            seen = set()
            for i in range(9):
                x = board[i][j]
                if x != ".":
                    if x in seen:
                        return False
                    seen.add(x)

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        x = board[i][j]
                        if x != ".":
                            if x in seen:
                                return False
                            seen.add(x)

        return True