A, B, M = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())
ab = min(a) + min(b)
for i in range(M):
    x, y, c = map(int, input().split())
    ab = min(ab, a[x - 1] + b[y - 1] - c)
print(ab)
