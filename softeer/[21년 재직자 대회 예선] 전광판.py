import sys
nums  = [[0,1,1,1,1,1,1],[0,1,0,0,0,0,1],[1,1,1,0,1,1,0],[1,1,1,0,0,1,1],[1,1,0,1,0,0,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[0,1,1,1,0,0,1],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

N = int(input())
for q in range(N):
    count = 0
    x1, y1 = input().split()
    x1 = x1.rjust(5, '*')
    y1 = y1.rjust(5, '*')

    for i in range(5):
        if x1[i] == '*' or y1[i] == '*':
            if x1[i] != y1[i]:
                if x1[i] == '*':
                    count += sum(nums[int(y1[i])])
                elif y1[i] == '*':
                    count += sum(nums[int(x1[i])])
        else:
            for j in range(7):
                if nums[int(x1[i])][j] != nums[int(y1[i])][j]:
                    count += 1
    print(count)
