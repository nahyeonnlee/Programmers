def solution(progresses, speeds):
    answer = []
    processed_date = [0] * len(progresses)
    
    for i in range(len(progresses)):
        days = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            days += 1
        processed_date[i] = days
    
    stack = []
    for day in processed_date:
        if not stack or day > stack[0]:
            if stack:
                answer.append(len(stack))
            stack = [day]  
        else:
            stack.append(day)
            
    if stack:
        answer.append(len(stack))
    
    
    return answer