class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dimensions of the grid
        rows = len(heights)
        cols = len(heights[0])

        # essential structures to hold the land coords
        p_queue = collections.deque()
        a_queue = collections.deque()
        p_seen = set()
        a_seen = set()

        # land coords bordering pacific ocean
        for c in range(cols):
            coords = (0, c)
            p_seen.add(coords)
            p_queue.append(coords)

        for r in range(rows):
            coords = (r, 0)
            p_seen.add(coords)
            p_queue.append(coords)

        # land coords bordering the atlantic ocean
        for r in range(rows):
            coords = (r, cols - 1)
            a_seen.add(coords)
            a_queue.append(coords)

        for c in range(cols):
            coords = (rows - 1, c)
            a_seen.add(coords)
            a_queue.append(coords)

        # perform bfs
        def bfs(q, seen):
            while q:
                r, c = q.popleft()

                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
                        seen.add((nr, nc))

        bfs(a_queue, a_seen)
        bfs(p_queue, p_seen)

        return list(a_seen & p_seen)