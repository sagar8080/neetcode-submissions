class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for token in tokens:
            if token == '+':
                add_back = stack.pop() + stack.pop()
                stack.append(add_back)
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                mul_back = stack.pop() * stack.pop()
                stack.append(mul_back)
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        
        return stack[0]