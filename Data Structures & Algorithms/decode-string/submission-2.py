class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr #this order since we are going backwards
                stack.pop() #remove that [

                mult = ''
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult #this order since we are going backwards
                stack.append(int(mult) * substr)
        return ''.join(stack)

