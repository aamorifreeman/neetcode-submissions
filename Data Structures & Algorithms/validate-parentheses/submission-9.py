"""
stack = []

stack.append(x)   # PUSH
stack.pop()       # POP + return top
stack[-1]         # PEEK
len(stack)        # SIZE
not stack         # IS EMPTY
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in pairs: #closed bracket
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack


        



        
        
        
            





        