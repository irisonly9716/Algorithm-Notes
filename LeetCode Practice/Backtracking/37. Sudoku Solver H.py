from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # approach:recursion by grid

        boxes = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) # int in sets
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[i//3][j//3].add(num)

        def dfs(row:int, col:int) -> bool:

            if row == 9:
                return True

            nxt_row = row + 1 if col == 8 else row
            nxt_col = col + 1 if col < 8 else 0

            # if the curr grid has a num, call recursion
            if board[row][col] != '.':
                if dfs(nxt_row, nxt_col):
                    return True

            # if not, fill num to grid
            else:
                for num in range(1, 10):
                    if num not in boxes[row//3][col//3] and num not in cols[col] and num not in rows[row]:
                        board[row][col] = str(num)
                        boxes[row//3][col//3].add(num)
                        cols[col].add(num)
                        rows[row].add(num)
                        
                        if dfs(nxt_row, nxt_col):
                            return True

                        boxes[row//3][col//3].remove(num)
                        cols[col].remove(num)
                        rows[row].remove(num)
                        board[row][col] = '.'

            return False

        dfs(0, 0)
                           



# O(9 ^ k) k is the num of blank grids
# O(9 ^ 2) 递归是按格子逐个推进的，不管当前格子有没有数字，都会调用一次 dfs(nxt_row, nxt_col)，所以递归深度固定是 81，而不是 k。