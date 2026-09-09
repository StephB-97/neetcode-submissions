class Node:
        def __init__(self, val = 0, prev = None, next = None):
            self.val = val
            self.prev = None
            self.next = None
class MyLinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next =  self.tail
        self.tail.prev = self.head
        self.size = 0
        


        

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if cur and cur != self.tail and index == 0:
            return cur.val
        
        return -1

        



        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
        
        
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.prev.next = new_node
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        self.size += 1
        

        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            new_node.prev = cur.prev
            new_node.next = cur
            cur.prev.next = new_node
            cur.prev = new_node
            self.size += 1
        
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.head.next
        while index > 0:
            cur = cur.next
            index -= 1

        cur.next.prev = cur.prev
        cur.prev.next = cur.next
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)