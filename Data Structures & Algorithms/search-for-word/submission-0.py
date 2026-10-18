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
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))  # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False