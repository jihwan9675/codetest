def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sub = nums[i]+nums[j]+nums[k]
                for z in range(2, sub):
                    if sub % z == 0:
                        break
                else:
                    answer+=1
    

    return answer
