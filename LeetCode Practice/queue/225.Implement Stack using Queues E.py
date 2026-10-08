import collections

# use only 1 queue to implement the stack.
# we need to add elements to the end of deque; when pop, check if 
class MyStack:

    def __init__(self):

        self.q = collections.deque()

    def push(self, x: int) -> None:

        # add to the tail of queue
        self.q.append(x)
        
    def pop(self) -> int:     

        # we are not allowed to invoke q.pop(), we can only use queue.popleft()
        # shffle len - 1 times, make the top element in the head; 
        # the rest queue will still in original order (tail is the top, head is the bottom)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    def top(self) -> int:

        # keep the tail of queue be the top of stack;
        # retrive the top element from the tail
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        top = self.q.popleft()
        self.q.append(top)

        return top


    def empty(self) -> bool:

        return not self.q

