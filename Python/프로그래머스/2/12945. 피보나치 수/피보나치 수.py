def solution(n):

    F_prev = 0 #F(0)=0
    F_now = 1 #F(1)=1
    F_fu = 1 #F(2)=1
    
    for i in range(2, n+1):
        F_fu = (F_now + F_prev) % 1234567 #F(n) = F(n-1) + F(n-2) 
        
        #다음 타임 스텝에 맞춰 업데이트
        F_prev = F_now 
        F_now = F_fu
     
    return F_now