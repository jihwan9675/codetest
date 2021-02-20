def solution(genres, plays):
    ls = dict()
    ls1 = dict()
    answer = []
    for i in range(len(genres)):
        if not genres[i] in ls1:
            ls1[genres[i]] = [plays[i]]
        else:
            ls1[genres[i]].append(plays[i])
    for i in range(len(genres)):
        if not genres[i] in ls:
            ls[genres[i]] = [plays[i]]
        elif len(ls[genres[i]])==1 and ls[genres[i]][0]>=plays[i]:
            ls[genres[i]].append(plays[i])
        elif len(ls[genres[i]])==1 and ls[genres[i]][0]<=plays[i]:
            ls[genres[i]].insert(0,plays[i])
        elif ls[genres[i]][0]<=plays[i]:
            ls[genres[i]][1]=ls[genres[i]][0]
            ls[genres[i]][0]=plays[i]
        elif ls[genres[i]][1]<=plays[i]:
            ls[genres[i]][1]=plays[i]

    li = list(ls)

    sub = []
    for i in range(len(li)):
        sub.append(sum(ls1[li[i]]))
    
    k = [p for p in enumerate(sub)]
    k.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(k)):
        for j in range(len(ls[li[k[i][0]]])):
            if not plays.index(ls[li[k[i][0]]][j]) in answer:
                answer.append(plays.index(ls[li[k[i][0]]][j]))
            else:
                answer.append(plays[plays.index(ls[li[k[i][0]]][j])+1:].index(ls[li[k[i][0]]][j])+plays.index(ls[li[k[i][0]]][j])+1)

    return answer
