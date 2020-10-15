def solution(x):
    st=str(x)
    ss=0
    for i in range(len(st)):
        ss+=int(st[i])
        
    if x%ss==0:
        return True
    else:
        return False
