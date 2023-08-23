A, B, C = map(int, input().split())

if A==B and B==C:
    print(10000+1000*A)
elif A==B or B==C:
    print(1000+100*B)
elif A==C:
    print(1000+100*A)
else:
    print(max(A,B,C)*100)
