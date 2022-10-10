def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    
    _minX = sizes[0][0]
    _minY = sizes[0][1]
    
    for i in range(1, len(sizes)):
        if sizes[i][0] > _minX:
            _minX = sizes[i][0]
        if sizes[i][1] > _minY:
            _minY = sizes[i][1]
        
    
    return _minX * _minY
