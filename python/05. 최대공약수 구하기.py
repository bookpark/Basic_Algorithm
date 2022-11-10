# a와 b의 최대공약수를 구하는 함수를 작성하시오.
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

print(gcd(4, 6))

# Euclid 방식을 이용해 최대공약수를 구하는 함수를 작성하시오.
# Euclid 방식: gcd(a, b) == gcd(b, a % b)
# 이 방식은 recursive function으로 풀 수 있음

def gcd(a, b):
    print("gcd: ", a, b)
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(81, 54))

# n번째 피보나치 수를 구하는 알고리즘을 recursive function을 이용해 구현해보시오.
def fibonacci(n):
    if n <= 1:
        return n
    # ex) 피보나치 수열에서의 7번 값 = 5번 값 + 6번 값
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(7))
