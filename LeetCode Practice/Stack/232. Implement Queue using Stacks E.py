# approach: use 2 stacks. When we need to pop an element, push all elements in in_stack to out_stack if out_stack is empty.
class MyQueue:

    def __init__(self):
        
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        
        self.in_stack.append(x)

    def pop(self) -> int:

        # if no out_stack, push elements to it.
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


        return self.out_stack.pop()


    def peek(self) -> int:

        # to avoid: no elements in the out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack[-1]


    def empty(self) -> bool:

        return not self.in_stack and not self.out_stack
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()