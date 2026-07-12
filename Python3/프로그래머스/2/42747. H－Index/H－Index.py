def solution(citations):

    citations.sort(reverse=True) #내림차순
    n = len(citations)
    answer = 0
    
    for i in range(n):
        # i+1번째 citations >= i+1
        # i+1개가 i+1번 이상 인용됨
        if citations[i] >= i + 1:
            answer = i + 1 # i+1 (=h)
        else:
            break
            
    return answer