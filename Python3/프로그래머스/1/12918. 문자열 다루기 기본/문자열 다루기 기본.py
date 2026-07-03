def solution(s):
    #문자열 길이가 4/6 아니면 False
    if len(s) != 4 and len(s) != 6:
        return False
    
    answer = True
    #숫자가 아니라면 False
    for i in s:
        if not i.isdigit():
            answer = False
    
    return answer