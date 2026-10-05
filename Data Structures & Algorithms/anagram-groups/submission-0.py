class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            if tuple(freq) not in output:
                output[tuple(freq)] = []

            output[tuple(freq)].append(s)

        return list(output.values())
        