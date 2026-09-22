from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    #스킬트리 하나씩 비교
    for st in skill_trees:
        #queue에 스킬 순서 담기 
        queue = deque(list(skill))
        
        #트리에서 뽑아온 하나의 스킬트리에 들어 있는 스킬과
        for s in st:
            #선행 스킬순서가 겹친다면
            if s in skill:
                #첫번째 선행 스킬순서와 같지 않다면 st 버리기
                if s != queue.popleft():
                    break
                    
        #안전하게 for문 돌았다면 +1
        else:
            answer += 1
        
    
    return answer