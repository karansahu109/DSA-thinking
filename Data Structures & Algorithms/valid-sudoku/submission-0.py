class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = collections.defaultdict(set)
        for i in range (9):
            verifierRow = set()
            for j in range (9):
                if board[i][j] not in verifierRow:
                    verifierRow.add(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False

        for i in range (9):
            verifierCol = set()
            for j in range (9):
                if board[j][i] not in verifierCol:
                    verifierCol.add(board[j][i])
                elif board[j][i] == ".":
                    continue
                else:
                    return False
        
        for i in range (9):
            for j in range (9):
                if board[i][j] not in box[(i//3, j//3)]:
                    box[(i//3, j//3)].add(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False
        return True



        