def solution(s):
    answer = 0
    cnt_1 = 0
    cnt_2 = 0
    
    x = ''
    
    for i in s:
        # x 할당
        if cnt_1 == 0 and cnt_2 == 0:
            x = i
         # x와 같은 문자일 때 카운트 
        if x == i:
            cnt_1 += 1
        # x와 다른 문자일 때 카운트
        else:
            cnt_2 += 1
    
        # 같아지면 answer += 1, 초기화
        if cnt_1 == cnt_2:
            answer += 1
            cnt_1 = 0    
            cnt_2 = 0
    
    #마지막 글자 예외 처리
    if cnt_1 != 0 or cnt_2 != 0:
        answer += 1
        
    return answer