def solution(n, words):
    answer = []

    for idx, word in enumerate(words):
        # 첫 단어는 무조건 리스트에
        if len(answer)==0: 
            answer.append(word)
            continue
        
        # 끝말잇기 조건을 만족한 경우 리스트에 추가
        if answer[-1][-1] == word[0] and word not in answer:
            answer.append(word)
        # 탈락한 경우
        else: 
            who = (idx+1) % n #몇번째 참가자인지
            if who == 0: who = n 
            when = (idx // n) + 1 #몇번째 턴인지
            
            return [who, when]

    return [0,0] #탈락 없는 경우