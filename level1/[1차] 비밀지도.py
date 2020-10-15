def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        ls=""
        a=format(arr1[i],'b').zfill(n)
        b=format(arr2[i],'b').zfill(n)
        
        for j in range(len(a)):
            if a[j]=="1" or b[j]=="1":
                ls+="#"
            else:
                ls+=" "
        answer.append(ls)
        
    return answer
