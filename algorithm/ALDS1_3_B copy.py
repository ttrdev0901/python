class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time

class Queue:
    def __init__(self):
        self.tasks = []
    
    def enqueue(self, task):
        self.tasks.append(task)
    
    def size(self):
        return len(self.tasks)

    def dequeue(self):
        return self.tasks.pop(0)

n, qtime = map(int, input().split())
queue = Queue()

for _ in range(n):
    name, time = input().split()
    task = Task(name, int(time))
    queue.enqueue(task)

elasped = 0
while queue.size() != 0:
    t = queue.dequeue()
    if qtime < t.time:
        elasped += qtime
        t.time -= qtime
        queue.enqueue(t)
    else:
        elasped += t.time
        print(t.name, elasped)

