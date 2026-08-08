def solution(numbers):
    list = []
    
    #리스트 앞에서부터 하나씩 i 설정
    for i in range(len(numbers)):
        #i 뒤에 있는 숫자들과 다 더하기
        for j in range(i + 1, len(numbers)):
            add_num = numbers[i] + numbers[j]
            
            #중복되지 않을 때만 리스트에 추가
            if add_num not in list:
                list.append(add_num)
        
    list.sort()
    
    return list