def solution(board, moves):
    answer = 0
    box=[]
    for i in range(len(moves)):
        for k in range(len(board)):
            if board[k][moves[i]-1]!=0:               
                if len(box)>0:
                    if box[len(box)-1]==board[k][moves[i]-1]:
                        answer+=2
                        box.pop()
                        board[k][moves[i]-1]=0
                        break
                box.append(board[k][moves[i]-1])
                board[k][moves[i]-1]=0    
                break
                    
    return answer
