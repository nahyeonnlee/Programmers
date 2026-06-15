def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    
    #2진수로 바꾸기
    for i in arr1:
        arr1_bin.append(bin(i)[2:].zfill(n))
    for i in arr2:
        arr2_bin.append(bin(i)[2:].zfill(n))
    
    #지도 겹쳐서 최종 지도 얻기
    for i in range(n):
        ans = ''
        
        for j in range(n):
            if (arr1_bin[i][j] == '0') and (arr2_bin[i][j] == '0'):
                ans += ' '
            else : 
                ans += '#'
        answer.append(ans)
        
    return answer