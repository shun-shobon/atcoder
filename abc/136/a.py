A, B, C = map(int, input().split())
D = C - (A - B)
print(0 if D < 0 else D)
