class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]
        if og == color:
            return image

        image[sr][sc] = color
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        rows = len(image)
        cols = len(image[0])
        q = deque([(sr, sc)])
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows)) and (c in range(cols)) and (image[r][c] == og):
                    image[r][c] = color
                    q.append([r,c])
        return image
