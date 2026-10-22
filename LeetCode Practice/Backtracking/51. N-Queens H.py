from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # approach:recursion, each recursive layer is a row; use sets to remove invalid columns and diagonals
        # rules:each row and each col only have 1 queen
        # use backtracking to try each possibility
        # use a board to record the current state of the board to save the result when we find a valid solution

        res = []
        cols = set()
        diag1 = set()
        diag2 = set()

        board = [['.'] * n for _ in range(n)]

        def backtracking(row) -> None:

            if row == n:
                res.append([''.join(row_data) for row_data in board])
                return

            # 尝试在当前行的每一个格子里面加入Q
            for col in range(n):

                d1 = row + col
                d2 = row - col

                if col not in cols and d1 not in diag1 and d2 not in diag2:

                    board[row][col] = 'Q'

                    cols.add(col)
                    diag1.add(d1)
                    diag2.add(d2)

                    backtracking(row + 1)

                    board[row][col] = '.' # backtrack
                    cols.remove(col)
                    diag1.remove(d1)
                    diag2.remove(d2)
                

        backtracking(0)

        return res

    # O(n!) time, O(n) space for recursion stack and sets
    # 这跟全排列是一个道理：每行选一个不同的列，本质上就是在枚举列号的排列。
    # #再加上对角线的剪枝，实际搜索量会比 n! 小得多，但面试和题解里一般就说 O(n!) 作为上界。