def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(': 
            stack.append(i)
        elif i == ')':
            if stack: 
                stack.pop()
            else: 
                return False
        else: 
            return False
    
    if len(stack) != 0: 
        answer = False

    return answer