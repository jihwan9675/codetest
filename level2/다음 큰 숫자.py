def solution(n):
    answer = 0
    sub = bin(n)[2:].count('1')
    for i in range(n+1, n*2+1):
        if bin(i)[2:].count('1') == sub:
            return i
