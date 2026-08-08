def solution(price, money, count):
    answer = 0
    money_need = 0
    
    for i in range(1,count+1): 
        money_need += price * i
    
    #부족하다면
    if money_need > money:
        answer = money_need - money
        
    return answer