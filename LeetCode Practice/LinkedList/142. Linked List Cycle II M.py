from typing import Optional

# Definition for singly-linked list.  
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # approach: Floyd two pointers. 
        # 1. "fast" goes 2 steps and "slow" goes 1 step at once. 
        # 2. when slow meets fast, we find the cycle. 
        # 3. send one pointer to the head, two pointers go syncronously, when they meet again, we find the entrance of the cycle.

        slow = fast = head

        # if fast reaches the end, no cycle.
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next

            # if cycle
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                
                return slow

        # if no cycle, we should return a None.
        return None


        # TC:O(n)
        # SC:O(1)

        


