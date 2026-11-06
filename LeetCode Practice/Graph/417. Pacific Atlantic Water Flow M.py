from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # approach: graph - reversely BFS
        # calculate the grids that water can reversely flow to from both oceans.
        # 反向bfs 搞bfs的helper 最后返回两个大洋能流到的格子的交集即可
        # 哪些格子能最终流向both 2个大洋？
        # 一些格子能流到大西洋，一些格子能流到太平洋，我们取交集即可。
        # 而且不需要正向洋流（更麻烦） 取巧从岛的边缘计算反向洋流即可

        n = len(heights)
        m = len(heights[0])
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # two lists of oceans' border grids
        atlantic = [(i, m - 1) for i in range(n)] + [(n - 1, j) for j in range(m)] 
        pacific = [(i, 0) for i in range(n)] + [(0, j) for j in range(m)]

        def bfs(starts:List[tuple[int, int]]) -> set[tuple[int, int]]:

            # we will return this visited set, as a record of every grid the current oceans can reach
            visited = set(starts) 
            queue = deque(starts)

            while queue:

                i, j = queue.popleft()

                for x, y in directions:
                    
                    new_i = i + x
                    new_j = j + y

                    # 1. in the grids 2. new grid >= old grid so that it can flow 3. not visited
                    if (new_i >= 0 and new_i < n and new_j >= 0 and new_j < m 
                    and (new_i, new_j) not in visited 
                    and heights[new_i][new_j] >= heights[i][j]):

                        visited.add((new_i, new_j))
                        queue.append((new_i, new_j))

            return visited

        atl_set = bfs(atlantic)
        pac_set = bfs(pacific)

        return [[i, j] for i, j in atl_set & pac_set]

# TC: O(n * m) each grid is visited at most once per ocean
# SC: O(n * m) visited sets + queue
