from collections import deque
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # approach: graph - find the shortest way (queue + state)
        # you can't turn the lock to deadends

        deadends = set(deadends)
        start = "0000"
        if target in deadends or start in deadends:
            return -1
        queue = deque()
        queue.append((start, 0)) # (current lock, times) # shorter times are always in the front of the queue
        visited = {start}


        while queue:

            lock, times = queue.popleft()

            if lock == target:
                return times

            # 4 digits * 2 ways (up and down)
            for i in range(4):
                num = int(lock[i])
                new_num1 = num + 1 if num < 9 else 0 # go up
                new_num2 = num - 1 if num > 0 else 9 # go down
                new_lock1 = lock[:i] + str(new_num1) + lock[i+1:]
                new_lock2 = lock[:i] + str(new_num2) + lock[i+1:]
                if new_lock1 not in deadends and new_lock1 not in visited:
                    visited.add(new_lock1)
                    queue.append((new_lock1, times+1))
                if new_lock2 not in deadends and new_lock2 not in visited:
                    visited.add(new_lock2)
                    queue.append((new_lock2, times+1))

        return -1

# TC: O(10^4) each lock is visited at most once
# SC: O(10^4) queue and visited set