def solution(clothes):
    dict = {}
    answer = len(clothes)
        
    for cth in clothes:
        if dict[cth[1]]:
            dict[clh[1]] += 1
        else:
            dict[cth[1]] = 1
        
        
    return dict