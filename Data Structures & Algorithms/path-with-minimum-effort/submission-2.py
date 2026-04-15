class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        hp = [[0, 0, 0]]
        vis= set()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        while hp:
            diff, r, c = heapq.heappop(hp)
            if (r, c) in vis:
                continue
            
            vis.add((r, c))

            if r == m - 1 and c == n - 1:
                return diff

            for k in range(4):
                x = r + dx[k]
                y = c + dy[k]
                if (0 <= x < m) and (0 <= y < n) and (x, y) not in vis:
                    new_diff = max(diff, abs(heights[x][y] - heights[r][c]))
                    heapq.heappush(hp, [new_diff, x, y])
        return 0

        
