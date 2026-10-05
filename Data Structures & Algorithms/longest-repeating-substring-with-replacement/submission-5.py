class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        globalmax = 0 
        l = 0 
        r = 0 
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) #.get curr val OR 0
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1 
                l += 1
            else:
                globalmax = max(globalmax, r - l + 1)
        return globalmax