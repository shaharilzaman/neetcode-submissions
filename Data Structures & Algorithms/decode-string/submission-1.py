class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                innerstr = ''
                while stack[-1] != '[':
                    innerstr = stack.pop() + innerstr
                stack.pop() #remove that [

                mult = ''
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult
                stack.append(int(mult) * innerstr)
        return ''.join(stack)
            