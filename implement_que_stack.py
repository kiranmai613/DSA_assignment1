class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val):
        self.stack1.append(val)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
q.enqueue(4)
print(q.dequeue())  # Output: 3
print(q.dequeue())  # Output: 4
print(q.dequeue())  # Output: None (or any other appropriate value)
