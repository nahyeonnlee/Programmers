def solution(brown, yellow):
    # 총 타일 수
    total = brown + yellow
    
    # 세로 = y일 때 완전 탐색 시작 (최소 3)
    for y in range(3, int(total**0.5) + 1): # 세로는 최대 sqrt(total)+1
        if total % y == 0: # 나누어 떨어져야 함
            x = total // y # 가로 = x  구하기
            
            #  구해진 x와 y가 노란색 개수 공식에 맞는지 검사
            if (x - 2) * (y - 2) == yellow:
                return [x, y] 