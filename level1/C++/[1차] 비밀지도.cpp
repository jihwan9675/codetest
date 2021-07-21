def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        line1=format(arr1[i],"b").zfill(n)
        line2=format(arr2[i],"b").zfill(n)
        ss=""
        for j in range(n):
            if line1[j] == "1" or line2[j] =="1":
                ss+="#"
            else:
                ss+=" "
        answer.append(ss)
    
    
    
    return answer
