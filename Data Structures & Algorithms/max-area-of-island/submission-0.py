class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1 or (r, c) in visited:
                return 0

            visited.add((r, c))
            count = 1

            for dr, dc in dir:
                count += dfs(r + dr, c + dc)
            return count

        max_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_count = dfs(r, c)
                    max_count = max(max_count, curr_count)
        return max_count

                    
        