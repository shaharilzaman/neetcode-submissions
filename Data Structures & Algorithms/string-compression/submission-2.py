class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0 
        i = 0 
        while i < len(chars):
            duplicates = 1 
            while (duplicates + i) < len(chars) and chars[duplicates + i] == chars[i]:
                duplicates += 1
            chars[insert] = chars[i]
            insert += 1
            if duplicates > 1:
                chars[insert : insert + len(str(duplicates))] = list(str(duplicates))
                insert += len(str(duplicates))
            i += duplicates
        return insert
            