# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        # edge case
        if not head:
            return None

        # prev should be None rather than dummy, no additional dummy head needed
        prev = None
        curr = head

        # reverse the pointers
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

# TC:O(n)
# SC:O(1)

