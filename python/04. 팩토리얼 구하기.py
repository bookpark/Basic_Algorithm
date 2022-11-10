# 1부터 n까지의 곱 구하기 (팩토리얼)
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

print(factorial(5))

# recursive function을 이용한 팩토리얼 구하기
def fact(n):
    if n <= 1:
        return 1
    # 팩토리얼 공식 n*(n-1)! 사용
    return n * fact(n - 1)

print(fact(5))

# 1부터 n까지의 합을 recursive function을 이용해 구하시오.
def sum_n(n):
    if n <= 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))

# recursive function을 이용해 최댓값을 찾으시오.
v = [17, 92, 18, 33, 58, 7, 33, 42]
def find_max(a):
    if len(a) == 1:
        return a[0]
    max = find_max(a[1:])
    return max if max > a[0] else a[0]

print(find_max(v))
