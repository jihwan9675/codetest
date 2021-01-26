def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    print(people)
    front = -1
    end = len(people)-1
    while front<end:
        front+=1
        if people[front]+people[end]<=limit:
            end-=1
            
        answer+=1

    return answer
