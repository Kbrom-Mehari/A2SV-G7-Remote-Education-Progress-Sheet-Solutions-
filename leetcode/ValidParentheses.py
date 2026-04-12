from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                top = stack[-1] if stack else None
                if top:
                    if top == '(' and c == ')' or top == '[' and c == ']' or top == '{' and c == '}':
                        stack.pop()
                    elif top in ')]}':
                        return False
                    else:
                        stack.append(c)
                else:
                    return False
        return not stack