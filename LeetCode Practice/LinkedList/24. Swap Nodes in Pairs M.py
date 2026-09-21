from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # approach:iterate two nodes at once, use dummy node to cover the edge case

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = dummy

        # use prev.next and prev.next.next to avoid exceeding the indexes.
        while prev.next and prev.next.next:

            first = prev.next
            second = prev.next.next

            # first, handle prev.next, make sure the node linked to the prev node from last iteration.
            prev.next = second

            # swap
            first.next = second.next
            second.next = first

            # maintain "prev"
            prev = first


        return dummy.next


# TC:O(n)
# SC:O(1)