# Definition for singly-linked list.
class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        
        # approach:when we find the node.val == val, make prev -> next

        if not head:
            return None

        # the "dummy" makes sure we include the edge case, when head.val == val
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy

        while curr != None:

            # when curr.val == val, prev should be the last node whose node.val != val
            if curr.val == val:
                prev.next = curr.next
            
            # when curr.val != val, prev can be curr.
            else:
                prev = curr

            # move curr to the next node.
            curr = curr.next

        return dummy.next


# test helpers
def build_list(values):
    # build a linked list from a python list, return the head
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    # print the linked list like: 1 -> 2 -> 3 -> None
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals + ["None"]))

# test
s = Solution()
tests = [
    ([1,2,6,3,4,5,6], 6),   # remove in the middle and at the end
    ([], 1),                # empty list
    ([7,7,7,7], 7),         # remove every node
    ([6,6,1,2], 6),         # head.val == val, the dummy node case
]
for values, val in tests:
    head = build_list(values)
    print(f"val={val}")
    print("before:", end=" ")
    print_list(head)
    print("after: ", end=" ")
    print_list(s.removeElements(head, val))
    print()

# TC:O(n)
# SC:O(1)