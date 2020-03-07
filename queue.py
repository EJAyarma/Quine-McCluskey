from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def __str__(self):
        return str(self.queue)

    def get_size(self):
        return len(self.queue)

myq = Queue()
myq.enqueue(3)
myq.enqueue(4)
print(myq)