import sys

#sys.stdin.readline().rstrip()
T = int(sys.stdin.readline().rstrip())
ls = []

for i in range(T):
    ls.append(sys.stdin.readline().rstrip())
    
ls = list(set(ls))
ls.sort()
ls.sort(key=len)

for p in ls:
    print(p)
