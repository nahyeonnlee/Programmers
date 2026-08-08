def solution(bridge_length, weight, truck_weights):
    time = 0 # 시간
    queue = truck_weights # 트럭 대기 공간
    bridge = [0] * bridge_length # 다리
    bridge_weight = 0 # 다리 무게
    
    # 대기 중인 트럭이 있거나 다리 위에 트럭이 있을 때만
    while queue or bridge_weight > 0:
        # 다리 위는 무조건 한 칸씩 전진 중
        out = bridge.pop(0)
        bridge_weight -= out 
        
        # 대기 중인 트럭이 있고 다리 무게를 초과하지 않는다면
        if queue and bridge_weight + queue[0] <= weight:
            # 다리 위에 트럭이 오른다
            bridge.append(queue[0])
            bridge_weight += queue[0]
            # 대기 줄에선 빠진다
            queue.pop(0)
            
        # 대기 트럭이 다리에 오르지 않는다면, 다리 오른쪽 끝엔 0을 채워 기존 트럭 전진
        else:
            bridge.append(0)
        
        time += 1   
            
    
    return time