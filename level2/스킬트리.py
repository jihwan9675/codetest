def solution(skill, skill_trees):
    answer = 0
    ls = list(skill)
    for i in range(len(skill_trees)):
        sub=[]
        for j in range(len(ls)):
            if skill_trees[i].find(ls[j]) == -1:
                sub.append(len(ls)+10)
            else:
                sub.append(skill_trees[i].find(ls[j]))
        if sub == sorted(sub):
            answer+=1
    return answer
