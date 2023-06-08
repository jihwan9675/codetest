def solution(s):
    answer = 0
    ls = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for p in ls:
        if p in s:
            s = s.replace(p, str(ls.index(p)))
            
    return int(s)
