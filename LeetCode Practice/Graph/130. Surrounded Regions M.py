class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # approach:graph - connected components
        # step 1. we iterate the edge first, mark "O" in the edge and all grid in its connected components to be "T". 
        # step 2. iterate the whole board, change all "O" to be "X"

        n = len(board)
        m = len(board[0])

        # dfs wash all nodes in the connected components to "T"
        def dfs(i, j) -> None:

            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == "X" or board[i][j] == "T":
                return

            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # iterate the edges
        for i in range(n):
            for j in [0, m - 1]:
                if board[i][j] == "O":
                    dfs(i, j)
        for i in [0, n - 1]:
            for j in range(m):
                if board[i][j] == "O":
                    dfs(i, j)
        
        # change all left "O" to "X"; all "T" to "O"
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X" 
                if board[i][j] == "T":
                    board[i][j] = "O"

# TC: O(n * m) each grid is visited a constant number of times
# SC: O(n * m) recursion stack in the worst case
