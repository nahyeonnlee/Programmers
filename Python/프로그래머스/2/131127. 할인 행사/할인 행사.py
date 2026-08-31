def solution(want, number, discount):
    answer = 0
    #want_number = {원하는 제품:개수}
    want_number = {}
    for i in range(len(want)):
        want_number[want[i]] = number[i]
    
    #discount_number = {세일하는 제품:개수}
    for i in range(len(discount)-9):
        discount_number = {}
        for item in discount[i:i+10]:
            discount_number[item] = discount_number.get(item,0) + 1
        #같으면 answer+=1
        if want_number == discount_number:
            answer += 1
        
    return answer