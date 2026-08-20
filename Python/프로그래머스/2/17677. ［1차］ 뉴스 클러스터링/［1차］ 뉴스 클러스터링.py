def solution(str1, str2):
    #소문자 변환
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = []
    list2 = []
    
    #영문자로 이루어진 경우만 각 리스트에 넣기
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            list1.append((str1[i]+str1[i+1]))
        
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            list2.append((str2[i]+str2[i+1]))
    
    #집합으로 변환(공통원소 제거됨)
    set1 = set(list1)
    set2 = set(list2)
    
    intersect = set1 & set2
    union = set1 | set2
    
    #두 리스트에서 교집합 원소 개수 최솟값들의 합
    intersect_num = sum(min(list1.count(x), list2.count(x)) for x in intersect)
    #두 리스트에서 합집합 원소 개수 최댓값들의 합
    union_num = sum(max(list1.count(x), list2.count(x)) for x in union)
    
    #공집합인 경우 유사도=1이므로 J = 1*65536 
    if union_num != 0 :
        J = intersect_num / union_num * 65536
    else:
        J = 65536
    
    return int(J)