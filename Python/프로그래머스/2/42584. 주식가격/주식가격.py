def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    stack = [] #주식의 인덱스 담는 스택
    
    for idx, price in enumerate(prices):
        #스택에 과거 주식이 들어있고, 스택 맨 위 주식가격이 현재가격보다 커진 경우
        while stack and prices[stack[-1]] > price:
            out = stack.pop()
            answer[out] = idx-out
        #스택에 인덱스 추가
        stack.append(idx)
    
    #스택에 남아 있는, 즉 가격이 떨어지지 않은 주식 처리
    while stack:
        out = stack.pop()
        answer[out] = (n - 1) - out
        
    return answer