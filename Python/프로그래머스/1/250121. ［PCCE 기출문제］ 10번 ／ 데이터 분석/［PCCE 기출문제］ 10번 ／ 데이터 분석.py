def solution(data, ext, val_ext, sort_by):
    answer = []
    
    if ext == 'code': cp = 0
    elif ext == 'date': cp = 1
    elif ext == 'maximum': cp = 2
    else: cp = 3
    
    for d in data:
        if d[cp] < val_ext:
            answer.append(d)
    
    if sort_by == 'code': sort_cp = 0
    elif sort_by == 'date': sort_cp = 1
    elif sort_by == 'maximum': sort_cp = 2
    else: sort_cp = 3
            
    answer = sorted(answer, key = lambda x: x[sort_cp])
    return answer