class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        # approach: monotonic stack
        # keeps the elements in stack DESC, calculate the distance between curr and stack[-1]

        m = len(temperatures)
        res = [0] * m
        stack = [] # DESC, index

        for index, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                curr_index = stack.pop()
                res[curr_index] = index - curr_index
            
            stack.append(index)

        return res
    
# TC:O(n) each element is pushed and popped at most once
# SC:O(n) stack