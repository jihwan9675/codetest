from collections import deque
import sys

N = int(input())

dq = deque()
_Slist = sys.stdin.readlines()

for i in range(N):
    Slist = _Slist[i].split()
    if Slist[0] == 'push':
        dq.append(int(Slist[1]))
    elif Slist[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif Slist[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif Slist[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif Slist[0] == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif Slist[0] == 'size':
        print(len(dq))
