class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                valid = len(stack) > 0 and\
                        ((c == ')' and stack[-1] == '(')\
                        or \
                        (c == ']' and stack[-1] == '[')\
                        or \
                        (c == '}' and stack[-1] == '{'))

                if valid:
                    stack.pop()
                else :
                    return False
        
        return len(stack) == 0  
                     
        