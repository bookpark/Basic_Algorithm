# for loop을 활용한 1부터 n까지의 합
def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(sum_n(50))

# for loop을 활용한 1부터 n의 제곱의 합
def sum_square_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** 2
    return s

print(sum_square_n(50))

# 가우스 공식을 활용한 1부터 n까지의 합
def sum_n(n):
    return n * (n + 1) // 2

print(sum_n(50))

# 가우스 공식을 활용한 1부터 n의 제곱의 합
def sum_square_n(n):
    return n * (n + 1) * (2 * n + 1) // 6

print(sum_square_n(50))
