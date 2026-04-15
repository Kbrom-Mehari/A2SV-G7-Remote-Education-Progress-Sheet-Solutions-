from collections import deque
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            op1 = 0
            op2 = 0
            res = 0
            if token in '+-*/':
                match token:
                    case '+':
                        op2 = stack.pop()
                        op1 = stack.pop()
                        res = op1 + op2
                        stack.append(res)
                    case '-':
                        op2 = stack.pop()
                        op1 = stack.pop()
                        res = op1 - op2
                        stack.append(res)
                    case '*':
                        op2 = stack.pop()
                        op1 = stack.pop()
                        res = op1 * op2
                        stack.append(res)
                    case '/':
                        op2 = stack.pop()
                        op1 = stack.pop()
                        res = op1 / op2
                        stack.append(math.trunc(res))
            else:
                stack.append(int(token))
        
        return stack[-1]