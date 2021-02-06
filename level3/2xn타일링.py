def solution(n):
    s1=1
    s2=1
    for i in range(n):
        s1, s2 = s2, s1+s2
        s2 = s2%1000000007
    return s2
