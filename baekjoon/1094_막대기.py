import math

T = int(input())
answer = 0

while T != 0:
    answer += 1
    T = T - 2**int(math.log2(T))
    
    
print(answer)
