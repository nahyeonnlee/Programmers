def solution(video_len, pos, op_start, op_end, commands):
    total_sec = int(video_len[0:2]) * 60 + int(video_len[3:5])
    current_sec = int(pos[0:2]) * 60 + int(pos[3:5])        
    op_start_sec = int(op_start[0:2]) * 60 + int(op_start[3:5])
    op_end_sec = int(op_end[0:2]) * 60 + int(op_end[3:5])
    
    if op_start_sec <= current_sec <= op_end_sec:
        current_sec = op_end_sec

    for c in commands:
        if c == 'prev':
            current_sec -= 10
        elif c == 'next':
            current_sec += 10
        if current_sec < 0:
            current_sec = 0
        if current_sec > total_sec:
            current_sec = total_sec
        if op_start_sec <= current_sec <= op_end_sec:
            current_sec = op_end_sec
            
    answer = f'{current_sec // 60 :02d}:{current_sec % 60 :02d}'
    return answer