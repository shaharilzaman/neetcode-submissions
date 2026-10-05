class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        r = 0
        globalmax = 0
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                currlen = r - l + 1
                globalmax = max(globalmax, currlen)
                r += 1
        return globalmax