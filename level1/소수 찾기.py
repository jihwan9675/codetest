def solution(n):
    n+=1
    sieve = [True] * (n)
    answer = 0
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:        
            for j in range(i+i, n, i):
                sieve[j] = False

    return len([i for i in range(2, n) if sieve[i] == True])
