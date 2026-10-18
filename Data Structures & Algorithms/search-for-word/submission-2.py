class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False 
        
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r not in range(rows) or c not in range(cols)
                or board[r][c] != word[i] or (r, c) in path):
                return False

            path.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            found = False
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    found = True
                    break
            path.remove((r,c))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False