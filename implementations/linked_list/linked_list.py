class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next: Node | None = None

class List:
    def __init__(self) -> None:
        self.head: Node | None = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self.head is None
    
    def value_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("List index out of range")
        
        curr = self.head

        for _ in range(index):
            if curr is None:
                raise IndexError("List index out of range")
            
            curr = curr.next

        if curr is None:
            raise IndexError("List index out of range")
        
        return curr.val
    
    def push_front(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
    
    def print(self):
        curr = self.head

        while curr is not None:
            print(str(curr.val) + ", ", end="")
            curr = curr.next
        print()

if __name__ == "__main__":
    my_list = List()
    my_list.push_front(0)
    my_list.push_front(12)
    my_list.push_front(3)
    my_list.print()
