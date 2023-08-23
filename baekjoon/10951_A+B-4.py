import sys

ls = sys.stdin.readlines()

for i in range(len(ls)):
    A,B = map(int,ls[i].split())
    print(A+B)
