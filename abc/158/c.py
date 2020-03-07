A, B = map(int, input().split())
a = [i for i in range(1, 1001) if int(i * 0.08) == A]
b = [i for i in range(1, 1001) if int(i * 0.1) == B]
c = set(a) & set(b)
if len(c):
    print(min(c))
else:
    print(-1)
