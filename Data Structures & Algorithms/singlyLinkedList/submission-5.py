class ListNode:
    def __init__(self, data):
        self.data = data
        self.link = None
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current.data
            current = current.link
            current_index += 1
        return -1


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.link = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        current = self.head
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return
        while current.link is not None:
            current = current.link
        current.link = new_node

    def remove(self, index: int) -> bool:
        current = self.head
        current_index = 0
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head.link
            return True
        while current_index < index - 1 and current is not None:
            current = current.link
            current_index += 1  
        if current is None or current.link == None:
            return False
        current.link = current.link.link
        return True
                      

    def getValues(self) -> List[int]:
        array = []
        current = self.head
        while current is not None:
            array.append(current.data)
            current = current.link
        return array
