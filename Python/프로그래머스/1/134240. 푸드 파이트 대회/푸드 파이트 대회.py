def solution(food):
    answer = ''
    half = '' 
    
    #0을 기준으로 왼쪽만 담기
    for i in range(1, len(food)):
        food_num = food[i] // 2
        half += str(i) * food_num
    
    #half + 0 + half 반대
    answer = half + '0' + half[::-1]
    
    return answer