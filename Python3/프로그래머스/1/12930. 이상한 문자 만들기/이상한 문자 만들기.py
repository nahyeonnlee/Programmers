def solution(s):
    answer = []
    words = s.split(' ')
    
    for w in words:
        new_word = ''
        #단어별로 변환
        for i in range(len(w)):
            if i%2 == 0:
                new_word += w[i].upper()
            else:
                new_word += w[i].lower()
                
        answer.append(new_word)
        
    answer = ' '.join(answer)
    
    return answer