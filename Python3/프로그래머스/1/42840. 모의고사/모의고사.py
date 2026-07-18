def solution(answers):
    spg1 = [1, 2, 3, 4, 5] #5개 반복
    spg2 = [2, 1, 2, 3, 2, 4, 2, 5] #8개 반복
    spg3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10개 반복
    
    spg_ans = {1:0, 2:0, 3:0} #맞춘 답 개수
    
    for idx, num in enumerate(answers):
        if num == spg1[idx%5]:
            spg_ans[1] += 1
            
        if num == spg2[idx%8]:
            spg_ans[2] += 1
            
        if num == spg3[idx%10]:
            spg_ans[3] += 1  
            
    max_score = max(spg_ans.values()) # 가장 많이 맞춘 사람의 정답 수
    answer = []
    
    for person, score in spg_ans.items(): 
        if score == max_score: #최대 정답 수와 같다면 해당 사람을 배열에 넣기
            answer.append(person)
    
    return answer