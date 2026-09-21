from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # approach:two pointers syncronously iterate the linked list. the distance of these two pointers should be n
        # and when the pointer "back" reaches the end, the pointer "front" is pointing to the previous node of the node should be removed.

        # edge case
        if not head:
            return None

        # use dummy node to cover the edge case that the head node should be deleted
        dummy = ListNode()
        dummy.next = head

        front = back = dummy

        # make distance between back and front
        for _ in range(n+1):
            back = back.next

        while back:
            front = front.next
            back = back.next

        front.next = front.next.next

        return dummy.next

# TC:O(n)
# SC:O(1)