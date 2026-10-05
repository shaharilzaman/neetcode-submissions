class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            key = tuple(freq)
            if key not in output:
                output[key] =[]
            output[key].append(s)
        return list(output.values())