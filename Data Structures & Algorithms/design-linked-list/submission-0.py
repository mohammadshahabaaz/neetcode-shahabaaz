class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next
        if curr is None:
            return -1
        return curr.val


    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        newNode = ListNode(val)
        cur = self.head
        for _ in range(index-1):
            if cur is None:
                return
            cur = cur.next
        if cur is None:
            return
        newNode.next = cur.next
        cur.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(index-1):
            if cur.next is None:
                return
            cur = cur.next
        if cur.next is None:
            return
        cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)