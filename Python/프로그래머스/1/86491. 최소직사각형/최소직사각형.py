def solution(sizes):
    for card in sizes:
        if card[0] < card[1]:
            card[0], card[1] = card[1], card[0]
    
    max_x = 0
    max_y = 0
    for card in sizes:
        if card[0] > max_x:
            max_x = card[0]
        if card[1] > max_y:
            max_y = card[1]
    
    answer = max_x * max_y
    return answer