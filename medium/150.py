class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", '/', '*'}
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append( a * b)
            else:
                stack.append(int(a / b))

        return stack [-1]
