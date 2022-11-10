# 원반이 n개 일 때 원반의 옮기는 순서를 출력하는 함수를 작성하시오.
def hanoi(n, start, end, mid):
    if n == 1:
        print(start, "->", end)
        return
    hanoi(n - 1, start, mid, end)
    print(start, "->", end)
    hanoi(n - 1, mid, end, start)

print("n = 3")
hanoi(3, 1, 3, 2)

# 알고리즘을 분석했을 때 원반 n층짜리 하노이의 탑을 옮기려면
#  원반을 모두 2n^2 - 1번 옮겨야 함

# recursive function을 이용한 그림 그리기
# 나무 그리기
import turtle as t

def tree(br_len):
    if br_len <= 5:
        return
    new_len = br_len * .7
    t.forward(br_len)
    t.right(20)
    tree(new_len)
    t.left(40)
    tree(new_len)
    t.right(20)
    tree(new_len)
    t.backward(br_len)

t.speed(0)
t.left(90)
tree(20)
t.hideturtle()
t.done()

# 시에르핀스키의 삼각형 그리기
import turtle as t

def tri(tri_len):
    if tri_len <= 10:
        for i in range(0, 3):
            t.forward(tri_len)
            t.left(120)
        return
    new_len = tri_len / 2
    tri(new_len)
    t.forward(new_len)
    tri(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)

t.speed(0)
tri(160)
t.hideturtle()
t.done()
