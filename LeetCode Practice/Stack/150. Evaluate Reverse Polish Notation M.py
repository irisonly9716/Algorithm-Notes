class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        # approach:stack. Store temporary results to stack, once we encounter a 
        # operation, pop top 2 from the stack and compute.
        # Mind the division between two integers always truncates toward zero.

        if not tokens:
            return 0

        stack = [] # stores integers.
        for token in tokens: # tokens are strings

            if token in {'+', '-', '*', '/'}:

                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2)) # truncate

            else:
                stack.append(int(token)) # stack stores int.

        return stack.pop()

# TC:O(n)
# SC:O(n) -> worst case: tokens = ["1", "2", "3", "4", "5", "+", "+", "+", "+"]