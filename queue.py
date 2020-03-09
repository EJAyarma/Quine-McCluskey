from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def __repr__(self):
        return str(self.queue)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)