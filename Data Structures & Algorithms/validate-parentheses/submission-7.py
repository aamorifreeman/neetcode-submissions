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
            if char in pairs:
                if not stack or stack[-1] != pairs[char]: #dont match
                    return False
                else: #does match
                    stack.pop()
            else:
                stack.append(char)
        return not stack



        
        
        
            





        