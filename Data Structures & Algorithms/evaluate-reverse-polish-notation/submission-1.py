class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))

            else:
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                if char == "+":
                    value = value1 + value2
                    stack.append(value)
                elif char == "-":
                    value = value1 - value2
                    stack.append(value)
                elif char == "*":
                    value = value1 * value2
                    stack.append(value)
                else:
                    value = int(value1 / value2)
                    stack.append(value)
        
        return stack[-1]


        

            