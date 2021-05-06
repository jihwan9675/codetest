def dfs(numbers, target, sum, i):
    count = 0
    if i == len(numbers):
        if sum==target:
            return 1
        return 0
    count += dfs(numbers, target, sum+numbers[i], i+1)    
    count += dfs(numbers, target, sum-numbers[i], i+1)    
    
    return count

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)
