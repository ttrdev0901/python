from collections import deque

deq = deque()

for i in range(int(input())):
    input_cmd = input()
    if input_cmd == 'deleteFirst':
        deq.popleft()
    elif input_cmd == 'deleteLast':
        deq.pop()
    else:
        cmd, x = input_cmd.split()
        if cmd == 'insert':
            deq.appendleft(x)
        elif cmd == 'delete':
            try:
                deq.remove(x)
            except:
                pass

print(*deq)