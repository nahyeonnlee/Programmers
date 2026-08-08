def solution(s):
    answer = 0
    stack = []
    
    for i in s:
        # 스택이 차있고 가장 위의 문자가 i랑 같다면
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        # 그 외 : 스택이 비어 있거나 i와 가장 위의 문자가 다르다면
        else:
            stack.append(i)
    

    if len(stack) == 0:
        answer = 1
            

    return answer