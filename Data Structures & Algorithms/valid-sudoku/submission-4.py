class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                b = (i // 3, j // 3)
                if val in rows[i] or val in cols[j] or val in box[b]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                box[b].add(val)

        return True   