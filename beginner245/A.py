a, b, c, d = map(int, input().split())

if a == c:
    if b <= d:
        print("Takahashi")
    else:
        print("Aoki")
elif a > c:
    print("Aoki")
else:
    print("Takahashi")