# 리스트 안의 동명이인을 찾아 집합으로 반환하시오.
name = ["Booki", "Jeeeun", "Jungwoo", "Booki"]
name2 = ["Booki", "Jeeeun", "Jungwoo", "Booki", "Jeeeun"]
def find_namesake(a):
    n = len(a)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

print(find_namesake(name))
print(find_namesake(name2))

# n명 중 두 명을 뽑아 짝을 짓는다고 가정할 때 짝을 지을 수 있는 모든 조합을 출력하시오. (중복 이름은 제외하시오.)
name3 = ["Chad", "Nick", "Matt", "Booki", "Jeeeun", "Nick", "Booki", "Chad"]
def match_two(a):
    l = list(set(a))
    n = len(l)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if not a[i] == a[j]:
                print(a[i] + " - " + a[j])

match_two(name3)
