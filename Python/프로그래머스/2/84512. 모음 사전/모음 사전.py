def solution(word):
    answer = 0
    #각 자리수가 바뀔 때마다 해당 자리 뒤에 있는 알파벳으로 만들 수 있는 경우의 수
    #즉 각 자리수가 바뀔 때마다 증가하는 숫자
    weights = [781, 156, 31, 6, 1]
    
    indexes = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    
    
    for idx, al in enumerate(word):
        #각 위치별로 알파벳 인덱스 * 위치별 가중치
        answer += indexes[al] * weights[idx] +1
        
    return answer