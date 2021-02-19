def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    check = [p for p in range(n)]
    
    for a, b, c in costs:
        if check[a] != check[b]:
            sub = check[b]
            for i in range(n):
                if check[i]==sub:
                    check[i]=check[a]
            answer+=c
            if check.count(check[0])==n:
                break
    return answer
