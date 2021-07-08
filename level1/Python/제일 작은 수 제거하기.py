def solution(arr):
    answer = []
    
    if len(arr)==1:
        return [-1]
    
    sub=arr[0]
             
    for i in range(1,len(arr)):
        if sub>arr[i]:
            sub=arr[i]        
    arr.remove(sub)
    return arr
