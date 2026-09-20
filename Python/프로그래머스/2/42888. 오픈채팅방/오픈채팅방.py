def solution(record):
    
    #최종 {id:nickname}
    id_nickname = {}
    for rec in record:
        words = rec.split(" ")
        if words[0] == "Enter" or words[0] == "Change":
            id_nickname[words[1]] = words[2]
    
    #채팅방 메시지
    result = []
    for rec in record:
        words = rec.split(" ")
        
        if words[0] == "Enter":
            nickname = id_nickname[words[1]]
            result.append(f"{nickname}님이 들어왔습니다.")
        
        elif words[0] == "Leave":
            nickname = id_nickname[words[1]]
            result.append(f"{nickname}님이 나갔습니다.")
            
    return result