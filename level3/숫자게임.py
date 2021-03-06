def solution(A, B):
    answer=0
    A.sort(reverse=True)
    B.sort(reverse=True)
    a=0
    b=0
    for i in range(len(B)):
        if A[a]<B[b]:
            answer+=1
            b+=1
        a+=1
    
    return answer
