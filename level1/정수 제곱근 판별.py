def solution(n):
    answer = 0
    if (n**0.5)==int(n**0.5):
        return (int(n**0.5)+1)*(int(n**0.5)+1)
    return -1
