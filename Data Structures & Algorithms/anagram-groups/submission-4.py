class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for str in strs:
            key = [0] * 26 
            for char in str:
                key[ord(char) - ord('a')] += 1 
            key = tuple(key)
            if key not in output:
                output[key] = []
            output[key].append(str)
        
        return list(output.values())
