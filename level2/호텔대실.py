def solution(book_time):
    imos = [0] * (24 * 60 + 10)
    cleantime = 10
    
    for start, end in book_time:
        st = start.split(':')
        ed = end.split(':')
        s = int(st[0]) * 60 + int(st[1])
        e = int(ed[0]) * 60 + int(ed[1])
        
        for i in range(s, e+10):
            imos[i] += 1
            
    return max(imos)
