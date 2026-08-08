def solution(people, limit):
    answer = 0
    
    people.sort()
    n = len(people)
    
    left = 0
    right = n-1
    
    while left <= right:
        #두 사람 태우는 경우
        if people[left] + people[right] <= limit:
            left += 1   
            right -= 1
            answer += 1
        #한 사람(무거운 사람)만 보내는 경우
        else:
            right -= 1
            answer += 1
            
    return answer