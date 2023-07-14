def solution(numbers):
    answer = [-1] * len(numbers)
    st = []
    
    for idx, number in enumerate(numbers):
        while st and numbers[st[-1]] < number:
            p = st.pop()
            answer[p] = number
        st.append(idx)
    
    
    return answer
