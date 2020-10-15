def solution(a, b):
    answer = ''
    answer_full = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    answer_num=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=4+b
    for i in range(0,a-1):
        day+=answer_num[i]   
    return answer_full[day%7]
