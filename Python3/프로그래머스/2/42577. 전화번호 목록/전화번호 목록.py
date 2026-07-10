def solution(phone_book):
    # 모든 전화번호:true를 해시 맵에 저장
    hash_map = {phone: True for phone in phone_book}
    
    # 각 전화번호의 접두어가 해시 맵에 존재하는지 확인
    for phone_num in phone_book:
        jumpto = ""
        # 번호의 글자를 하나씩 이어 붙여 접두어를 만듦 
        for char in phone_num[:-1]:
            jumpto += char
            # jumpto가 해시 맵에 들어있는지 검사
            if jumpto in hash_map:
                return False
                
    return True