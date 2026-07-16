class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # constants
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # starting position of the search
        start_vertex = (0, 0)
        queue.append(start_vertex)
        visited.add(start_vertex)
        length = 0
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                for dr, dc in directions:
                    boundary_condition = min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols
                    visit_condition = (r + dr, c + dc) in visited
                    if boundary_condition or visit_condition or grid[r + dr][c + dc] == 1:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1
        return -1