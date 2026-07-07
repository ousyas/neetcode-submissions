import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in ['+','*','-','/']:
                stack.append(int(char))
                print(stack)
            elif char == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1+v2)
                print(stack)
            elif char == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2-v1)
                print(stack)
            elif char == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2/v1))
                print(stack)
            elif char == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1*v2)
                print(stack)
        return stack[0]