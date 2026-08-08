def solution(A,B):
    answer = 0
    
    #오름차순 정렬
    A.sort()
    B.sort()
    
    n = len(A)
    
    #(A 오름차순) * (B 내림차순)
    for i in range(n):
        answer += A[i] * B[n-i-1]

    return answer