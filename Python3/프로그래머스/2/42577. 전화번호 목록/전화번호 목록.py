def solution(phone_book):
    
    # 순서대로 정렬
    phone_book.sort()
    
    # 정렬 시 접두어가 있다면 바로 뒤에 있을 것
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False 
        
    return True