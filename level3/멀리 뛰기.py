import math
def solution(n):
    ls = [1 for _ in range(n)]
    answer = 1
    
    for i in range(n//2):
        ls[i]=2
        ls[n-i-1]=0
        num1 = ls.count(1)
        num2 = ls.count(2)
        num = num1 + num2
        if num1<num2:
            num1, num2 = num2, num1
        sub =1
        sub1 = 1
        for j in range(1,num-num1+1):
            sub*=j
            sub1*=num-j+1
        answer+=sub1//sub
    
    return answer%1234567
