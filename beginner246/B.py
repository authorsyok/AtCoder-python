import math

a, b = map(int, input().split())
s = math.sqrt(a ** 2 + b ** 2)
print(a / s, b / s)