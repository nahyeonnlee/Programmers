def solution(participant, completion):
    # 해시 이용한 풀이
    hash = {}
    
    # 참가 선수명:등장횟수 
    for i in participant:
        if i in hash:
            hash[i] += 1
        else: 
            hash[i] = 1
    
    # 완주한 선수는 1 차감
    for j in completion:
        hash[j] -= 1
    
    # 완주하지 못한 선수 찾기
    for key in hash:
        if hash[key] > 0:
            answer = key
            
    return answer