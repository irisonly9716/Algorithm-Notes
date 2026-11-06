class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        
        # 岛屿的周长 每个格子先算4条边 如果两两相连就要剪掉2条边
        # Approach: iteration the whole grid, how many grids are connected?
        # perimeter = 4 * lands - 2 * number of connected 2 lands

        n = len(grid)
        m = len(grid[0])
        connected_count = 0
        lands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    lands += 1
                    # vertically connected
                    if i > 0 and grid[i - 1][j] == 1:
                        connected_count += 1
                    # horizontally connected
                    if j > 0 and grid[i][j - 1] == 1:
                        connected_count += 1    

        perimeter = lands * 4 - 2 * connected_count
        return perimeter            
    
# TC: O(n * m) iterate the whole grid
# SC: O(1) no extra space used

