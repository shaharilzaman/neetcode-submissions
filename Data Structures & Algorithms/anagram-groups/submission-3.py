class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #intiate a dictionary a -> #
        #iterate each word and get a numeric val use (abc = 1 + 2 + 3)
        #create dict where sum -> words of that sum
        #return the values per sum
        output = {}
        for word in strs:
            value = [0] * 26
            for char in word:
                value[ord(char) - ord('a')] += 1 
            key = tuple(value) 
            if key not in output:
                output[key] = []
            output[key].append(word)
        return list(output.values())
