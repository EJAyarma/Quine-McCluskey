a = []
b = 4
a.append(b)
print(a, b)
from queue import Queue
q1 = Queue()
q1.enqueue(5)
q2 = Queue()
q2.enqueue(6)
a.extend([q1, q2])
print(a)
print(q1)