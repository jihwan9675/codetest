import heapq
from collections import deque

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while scoville[0]<K:
        if len(scoville)==1:
            return -1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (s1+s2*2)) 
        answer+=1

    return answer
