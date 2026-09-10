from collections import deque

def solution(maps):
    #maps nxm
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy =  [0,0,-1,1]
    
    #큐에 기준 좌표를 담기
    queue = deque([(0,0)])
     
    while queue: 
        current = queue.popleft()
        
        #큐에 있던 좌표에서 상하좌우 이동
        for i in range(4):
            move_x = current[0] + dx[i]
            move_y = current[1] + dy[i]
            
            #이동한 좌표가 맵을 벗어나지 않았고, 갈 수 있는 길일 떄
            if 0 <= move_x < n and 0 <= move_y < m and maps[move_x][move_y] == 1:
                #이동한 좌표에 기준점(current)좌표 값+1 해서 큐에 담기
                maps[move_x][move_y] = maps[current[0]][current[1]] + 1
                queue.append((move_x, move_y))

    #종착 좌표 값
    if maps[n-1][m-1] == 1: 
        answer = -1
    else: 
        answer = maps[n-1][m-1]
    
    return answer