def solution(arr):
    answer = [arr[0]]
    check=arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            answer.append(arr[i])
            check=arr[i]
    return answer
