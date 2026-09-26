from typing import List, Optional

class TreeNode:

    def __init__(self, val="", left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildRPNTree(self, tokens: List[str]) -> Optional['TreeNode']: # 返回tree root


        # 变种题：如果构建这个逆波兰表达式的树？
        if not tokens:
            return None

        stack = [] # node
        operators = {'+', '-', '*', '/'}

        for token in tokens:

            # if num_string
            if token not in operators:

                node = TreeNode(token)
                stack.append(node)

            # if operators, pop num_string as subtrees
            else:
                
                node = TreeNode(token)
                node.right = stack.pop() # the first node popped from stack is the right node
                node.left = stack.pop()

                stack.append(node)


        return stack.pop() # the root is the only element in the stack


    # 把这颗树再算出结果？ 回溯
    def evaluate(self, root):

        # 叶子节点一定是值 先到叶子节点取值返回到上层
        if not root.left and not root.right:
            return int(root.val)

        left = self.evaluate(root.left)
        right = self.evaluate(root.right)

        if root.val == '+':
            return left + right
        elif root.val == '-':
            return left - right
        elif root.val == '*':
            return left * right
        else:
            return int(left / right)