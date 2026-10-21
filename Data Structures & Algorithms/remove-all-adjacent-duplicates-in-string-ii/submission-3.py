class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            if k == stack[-1][1]:
                stack.pop()
        
        output = ''
        for char, count in stack:
            output += char*count
        return output