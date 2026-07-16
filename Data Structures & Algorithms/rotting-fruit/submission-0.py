class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh, time = 0, 0
        queue = deque()

        # iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        # implement a BFS
        # loop over elements in the queue until
        # all the fresh oranges are rotten
        while queue and fresh > 0:
            queue_length = len(queue)
            for iteration in range(queue_length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    curr_r, curr_c = r + dr, c + dc
                    condition = (0 <= curr_r < ROWS) and (0 <= curr_c < COLS) and (grid[curr_r][curr_c] == 1)
                    if condition:
                        grid[curr_r][curr_c] = 2
                        queue.append((curr_r, curr_c))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                
                
        