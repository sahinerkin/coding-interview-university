class CircularQueue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.read = 0
        self.write = 0
    
    def enqueue(self, value) -> None:
        if self.full():
            raise OverflowError("Queue full")
        
        self.queue[self.write] = value
        self.write = (self.write + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("Queue empty")
        
        val = self.queue[self.read]
        self.read = (self.read + 1) % self.capacity
        self.size -= 1

        if self.size == 0:
            self.read = self.write = 0
        
        return val

    def empty(self) -> bool:
        return self.size == 0
    
    def full(self) -> bool:
        return self.size == self.capacity
    
    def print_queue_arr(self) -> None:
        print(self.queue)
    
    def print_queue(self) -> None:
        if self.write > self.read:
            print(self.queue[self.read:self.write])
        else:
            print(self.queue[self.read:] + self.queue[:self.write])
    
if __name__ == "__main__":
    queue = CircularQueue(5)

    queue.enqueue(5)
    queue.enqueue(12)
    queue.enqueue(7)
    queue.print_queue()
    queue.enqueue(10)
    queue.enqueue(102)
    queue.print_queue()

    val = queue.dequeue()
    print("Dequeued", val)

    val = queue.dequeue()
    print("Dequeued", val)
    queue.print_queue()