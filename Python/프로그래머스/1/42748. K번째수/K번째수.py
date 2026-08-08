def solution(array, commands):
    answer = []
    for new_com in commands: 
        new_arr = array[new_com[0]-1:new_com[1]]
        new_arr.sort()
        answer.append(new_arr[new_com[2]-1])
    
    return answer