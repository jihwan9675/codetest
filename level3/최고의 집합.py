def solution(n, s):
    if n>s:
        return [-1]
    ls =[]
    for i in range(n):
        if (s//n)* n != s:
            ls.append(s//n+1)
        else:
            ls.append(s//n)
        s=s-ls[-1]
        n-=1
    return sorted(ls)
