class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                box = (i // 3, j// 3)
                
                if val in rows[i] or val in cols[j] or val in square[box]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                square[box].add(val)

        return True
        



        