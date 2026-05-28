def solution(N, stages):
    fail_rates = {}
    total_player = len(stages)

    for stage in range(1, N+1):
        if total_player > 0:
            not_cleared = stages.count(stage)
            fail_rates[stage] = not_cleared / total_player
            total_player -= not_cleared
        else:
            fail_rates[stage] = 0
    
    answer = sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)
    return answer