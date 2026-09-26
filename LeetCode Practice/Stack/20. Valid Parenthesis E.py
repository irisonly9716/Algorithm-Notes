class Solution:
    def isValid(self, s: str) -> bool:


        # approach: stack + dict
        # if we encounter a pair, stack.pop(), else false.
        # check in the end if the stack is empty

        chars_dict = {'(':')', '[':']', '{':'}'}
        stack = []

        for char in s:

            if char in chars_dict:
                stack.append(char)
            else:
                # if the current char is a close and no stack, false
                # if the current char is a close but stack[-1] is not the open, false
                if not stack or char != chars_dict[stack[-1]]:
                    return False
                else:
                    stack.pop()

        # check if the stack is empty, if not, we got more open than close
        return not stack  
