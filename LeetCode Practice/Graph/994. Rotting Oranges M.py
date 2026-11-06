from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Approach: undirected graph; multi-origins BFS
        # rotten by layer

        n = len(grid)
        m = len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fresh = 0
        queue = deque()
        # count how many fresh oranges we have, if no one, return 0
        # add all rotten oranges into queue, as the first layer of rotten ones.
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        # ⭐
        if fresh == 0:
            return 0

        time = 0

        while queue:
            time += 1 # every layer + 1 minute
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in DIRECTIONS:
                    new_i = x + i
                    new_j = y + j
                    # if in bound and fresh, add to queue as next layer
                    if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 0
                        queue.append((new_i, new_j))
                        fresh -= 1
                        # if no fresh orange, return the curr time.
                        if fresh == 0:
                            return time
        
        return -1

# TC: O(n * m) each grid is enqueued at most once
# SC: O(n * m) queue
