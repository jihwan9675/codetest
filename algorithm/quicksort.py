def quick_sort(arr): # 분할정복 - 퀵정렬
    if len(arr) <= 1: # 배열의 크기가 1이하인 경우
        return arr
    pivot = arr[len(arr)//2] # 배열의 가운데 요소의 값
    less_arr, equal_arr, big_arr = [], [], [] # 분할정복을 위한 배열
    for i in arr:
        if i < pivot: # 가운데 요소의 값보다 작으면
            less_arr.append(i) # 작다는 배열에 삽입
        elif i > pivot: # 가운데 요소의 값보다 크면
            big_arr.append(i) # 크다는 배열에 삽입
        else: # 같다면
            equal_arr.append(i) # 같다는 배열에 삽입
    return quick_sort(big_arr) + equal_arr + quick_sort(less_arr) # 재귀 (분할정복)

# Test Code
print(quick_sort([5,6,11,33,14]))
