def solution(s, skip, index):
    answer = ''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for p in skip:
        alphabet = alphabet.replace(p ,'')
    for p in s:
        answer += alphabet[(alphabet.index(p)+index)%len(alphabet)]
    return answer
