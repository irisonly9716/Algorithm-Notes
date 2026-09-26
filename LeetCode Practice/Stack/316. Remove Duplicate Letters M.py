class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # approach: monotonic stack + hashmap + set
        # 1. use a dict to record the last appears of letters.
        # 2. iterate the string, keep the stack monotonic. 
        # 3. If we encounter a letter that is smaller and stack[-1] will appear again, pop stack[-1]


        last = {}

        for index, char in enumerate(s):
            last[char] = index

        stack = []
        seen = set() # a set for recording the existing letters in stack

        for index, char in enumerate(s):
            
            # when char is already in the stack, skip it, ensuring no duplicate letters.
            if char in seen:
                continue

            # for keeping stack monotonic 
            while stack and char < stack[-1] and last[stack[-1]] > index:

                seen.remove(stack.pop())

            seen.add(char)
            stack.append(char)
    
        return "".join(stack)

# TC:O(n)
# SC:O(26) the stack, last and seen hold at most 26 different lowercase letters.