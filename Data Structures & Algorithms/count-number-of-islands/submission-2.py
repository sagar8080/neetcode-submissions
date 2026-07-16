class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        if not grid:
            return islands
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(ro, cl):
            queue = collections.deque()
            queue.append([ro, cl])
            visited.add((ro, cl))
            while queue:
                curr_r, curr_c = queue.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    row, col = curr_r + dr, curr_c + dc
                    if 0 <= row < rows and 0 <= col < cols:
                        if grid[row][col] == "1" and (row, col) not in visited:
                            queue.append((row, col))
                            visited.add((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands