"""
Understand:
Given strings that represent maths in postfix notion, calculate the result of evaluationg that expression.

Plan:
    if length of tokens is 0:
        return 0
    stack = []
    for each string in tokens:
        if its a number,
            then convert it to integer and push it onto the stack
        otherwise 
            let second be the first popped value from stack
            let first be the second poppped value from stack
            Then if its +
                add and push the result into the stack
            Do the same for each possible operand
    if len(stack) == 1:
        return that
    else:
        return 0 or some error

        

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isNumber(token):
            try:
                float(token)
                return True
            except ValueError:
                return False
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            if isNumber(token):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                result = 0
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                else:
                    result = int(first / second)
                stack.append(result)
        if len(stack) == 1:
            return stack[0]
        else:
            return 0
        