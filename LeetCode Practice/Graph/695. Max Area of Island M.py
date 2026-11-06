from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Approach: Undirected Graph - find the biggest connected component
        # BFS/DFS

        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:

                    # BFS, create a new queue to iterate all adjacent grids
                    queue = deque() 
                    queue.append((i, j))
                    grid[i][j] = 0
                    area = 0

                    while queue:
                        i, j = queue.popleft()
                        area += 1
                        for x, y in DIRECTIONS:
                            new_i = i + x
                            new_j = j + y
                            # ⭐in the bound and == 1
                            if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m and grid[new_i][new_j] == 1:
                                queue.append((new_i, new_j))
                                grid[new_i][new_j] = 0

                    max_area = max(max_area, area)

        return max_area




        '''
        # DFS 图找最大连通分量
        

        n = len(grid)
        m = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        best = 0

        # just modify the 1 that has been visited to 0
        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    # 注意初始化一个size
                    curr_size = 1
                    queue = deque([(i, j)])
                    grid[i][j] = 0

                    while queue:

                        x, y = queue.popleft()

                        for direction in directions:
                            new_i = x + direction[0]
                            new_j = y + direction[1]

                            # 1. in the bound? 2. == 1?
                            if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m and grid[new_i][new_j] == 1:
                                grid[new_i][new_j] = 0
                                queue.append((new_i, new_j))
                                curr_size += 1

                    best = max(best, curr_size) # 在if里面记录best

        return best
        '''

# TC: O(n * m) each grid is visited at most once
# SC: O(n * m) queue in the worst case (whole grid is land)
