#include<set>
def solution(numbers):
    answer = []
    sub=[]
    for i in range(len(numbers)):
        for k in range(i+1,len(numbers)):
            #if sub.index(numbers[i]+numbers[k])==-1:
            sub.append(numbers[i]+numbers[k])
    
    sub2=set(sub)
    sub=list(sub2)
    sub.sort()
    return sub
