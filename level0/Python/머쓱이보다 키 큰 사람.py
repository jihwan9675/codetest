def solution(array, height):
    answer = 0
    
    for i in range(len(array)):
        if array[i] > height:
            answer += 1
    
    return answer머쓱이보다 키 큰 사람
