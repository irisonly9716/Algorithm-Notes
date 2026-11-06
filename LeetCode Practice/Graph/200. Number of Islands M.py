from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Approach: Undirected graph - BFS/DFS
        # every time we meet a "1", count += 1, then wash all the connected components to "0"

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] 
        count = 0
        n = len(grid) # rows
        m = len(grid[0]) # cols

        def dfs(row, col) -> None:

            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == "0":
                return
            
            # modify
            grid[row][col] = "0"

            for i, j in directions:
                dfs(row + i, col + j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
        
# we can also use a queue to do BFS, but DFS is easier to implement recursively
# O(n * m) time complexity, O(n * m) space complexity for the recursion stack