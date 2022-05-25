xy = [tuple(map(int, input().split())) for _ in range(3)]

ans_x, ans_y = 0, 0

for x, y in xy:
    ans_x ^= x
    ans_y ^= y
print(ans_x, ans_y)