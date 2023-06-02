def solution(park, routes):
    answer = []
    
    row = 0
    column = 0
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                row = i
                column = j

    for route in routes:
        flag = False
        ls = route.split(' ')
        distance = int(ls[1])
        
        if route[0] == 'E' and distance + column < len(park[0]) and distance + column >= 0:
            for i in range(1, distance + 1):
                if park[row][column+i] == 'X':
                    flag = True
                    break
            if flag == False:
                column += distance
        elif route[0] == 'S' and distance + row < len(park) and distance + row >= 0:
            for i in range(1, distance + 1):
                if park[row+i][column] == 'X':
                    flag = True
                    break
            if flag == False:
                row += distance
        elif route[0] == 'W' and column - distance >= 0 and column - distance < len(park[0]):
            for i in range(1, distance + 1):
                if park[row][column-i] == 'X':
                    flag = True
                    break
            if flag == False:
                column -= distance
        elif route[0] == 'N' and row - distance >= 0 and row - distance < len(park):
            for i in range(1, distance + 1):
                if park[row-i][column] == 'X':
                    flag = True
                    break
            if flag == False:
                row -= distance
    
    return [row, column]
