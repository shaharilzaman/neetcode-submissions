class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        globmax = 0
        l = 0
        r = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                currmax = r - l + 1
                globmax = max(globmax, currmax)
                r += 1 

        return globmax