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
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        for char in s:
            if char in closeToOpen: #closed bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else: #open bracket
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False





        