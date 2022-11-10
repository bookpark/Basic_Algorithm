# 17, 92, 18, 33, 58, 7, 33, 42 중에서 최댓값을 찾으시오.
def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(v))

# 리스트에 숫자가 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘을 만들어보시오.
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max_idx(v))

# 최솟값을 구하시오.
def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1, n):
        if a[i] < min_v:
            min_v = a[i]
    return min_v

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_min(v))
