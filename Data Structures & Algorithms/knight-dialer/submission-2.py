class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10 
        jumps = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        counts = [1] * 10
        mod = 10**9 + 7
        for _ in range(n-1): #wen arleady included 1 way in counts 
            jump_counts = [0] *10 #the counts for everyhting we cna get to from a particular digit
            for n in range(10):
                for jump in jumps[n]:
                    jump_counts[jump] = (jump_counts[jump] + counts[n]) % mod
            counts = jump_counts
        return sum(counts) % mod
