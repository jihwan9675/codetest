def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        cpy_arr=array[commands[i][0]-1:commands[i][1]]
        cpy_arr.sort()
        answer.append(cpy_arr[commands[i][2]-1])
    return answer
