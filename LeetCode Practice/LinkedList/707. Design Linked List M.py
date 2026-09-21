# approach:OOD, define the ListNode first and then design the LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        
        # design a dummy node as a field, ensuring the edge cases are included
        # able to add node at head
        self.dummy = ListNode()
        self.size = 0

    # O(n) O(1)
    def get(self, index: int) -> int:
        
        if index >= self.size:
            return -1

        curr = self.dummy
        for _ in range(index + 1):
            curr = curr.next

        return curr.val

    # O(1) O(1)
    def addAtHead(self, val: int) -> None:

        node = ListNode(val, self.dummy.next)
        self.dummy.next = node
        self.size += 1

    # O(n) O(1)
    def addAtTail(self, val: int) -> None:
        
        # iterate to the end and add the node
        # mind to change the link
        curr = self.dummy
        while curr.next:
            curr = curr.next

        node = ListNode(val)
        curr.next = node
        self.size += 1

    # O(n) O(1)
    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:
            return
        
        # this includes the edge that index == size == 0
        if index == self.size:
            self.addAtTail(val)
            return

        # iterate curr to the previous node of the index
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
            
        node = ListNode(val)
        node.next = curr.next
        curr.next = node
        self.size += 1
        
    #O(n) O(1)
    def deleteAtIndex(self, index: int) -> None:

        if index >= self.size:
            return

        # iterate curr to the previous node of the index
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        # cut the link
        curr.next = curr.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)