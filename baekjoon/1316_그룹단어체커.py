import sys

T = int(sys.stdin.readline().rstrip())
answer = 0

for i in range(T):
    temp = sys.stdin.readline().rstrip()
    checklist = []
    check = ''
    for p in temp:
        if check != p and p not in checklist:
            check = p
            checklist.append(p)
        elif check != p and p in checklist:
            break
    else:
        answer += 1
        
print(answer)
