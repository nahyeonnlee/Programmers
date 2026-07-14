def solution(clothes):
    dict = {} # (종류:개수)를 저장하기 위한 딕셔너리
        
    for name, kind in clothes:
        # 기존에 있는 종류면 1 더하고, 아니라면 0에서 시작해 1 더하기
        dict[kind] = dict.get(kind, 0) + 1
    
    # 경우의 수 구하는 법:
    # 하나의 종류마다 가능한 방법은 (1선택,2선택,..,선택안함)
    # 즉, (종류1+1) * (종류2+1) + ...
    answer = 1
    for cnt in dict.values():
        answer *= (cnt+1)
    
    # 모두 선택안함을 고른 경우 뺴기
    answer -= 1
        
    return answer