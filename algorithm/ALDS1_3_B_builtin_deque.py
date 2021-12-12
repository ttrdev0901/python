from collections import deque

class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time

n, qtime = map(int, input().split())
queue = deque([]) # 初期化

for _ in range(n):
    name, time = input().split()
    queue.append(Task(name, int(time)))

elasped = 0
while len(queue) > 0:
    task = queue.popleft()
    if task.time > qtime:
        task.time -= qtime
        elasped += qtime
        queue.append(task)
    else:
        elasped += task.time
        print(task.name, elasped)

