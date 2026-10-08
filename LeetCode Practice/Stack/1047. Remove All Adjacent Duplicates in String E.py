class Solution:
    def removeDuplicates(self, s: str) -> str:
        

        # 只要遍历字符串s 用一个stack来只要栈顶元素和现在遍历的一样的 就pop掉栈顶元素
        
        stack = []

        for char in s:

            if not stack or stack[-1] != char:
                stack.append(char)

            else:
                stack.pop()

        return ''.join(stack)



        