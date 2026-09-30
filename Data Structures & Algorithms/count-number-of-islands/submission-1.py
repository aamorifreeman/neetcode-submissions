class Solution:
    """
    r < 0 -> over top
    r >= len(grid) -> past bottom

    c < 0 -> over left
    c >= len(grid[0]) -> past right
    
    dir = []
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            
            #constraints/base case
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1' or (r, c) in visited:
                return 0

            visited.add((r, c))

            # process node
            for dr, dc in dir:
                dfs(r + dr, c + dc)
            return 1
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += dfs(r, c)
        return count






