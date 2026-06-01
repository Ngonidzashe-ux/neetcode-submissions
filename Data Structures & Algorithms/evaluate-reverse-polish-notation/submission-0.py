"""
Understand
1. Given a bunch of tokens with operators and operands, arrange them in a way that evaluates the expression and return the result.
2. Edge cases, just a bunch of numbers with nothing or bunch of operands without the numbers
3. Constraints. Token length is always gonna be at least one, no division by zero, 


Match.
Like valid paranthesis, use a stack, push the opening brackets onto the stack and pop when you find a closing bracket
Push numbers on the stack and then pop when you find an operator
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))

            else:
                stack.append(int(token))
        return stack[0]
        

        



        