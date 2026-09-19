def solution(arr):
    
    #최대공약수 구하는 함수
    def gcd(a,b):
        while b > 0:
            a,b = b, a%b
        return a
    
    
    a = arr[0]
    #최소공배수 = 두수의 곱/최대공약수
    for b in arr:
        a = (a*b) / gcd(a,b)
    
    return a