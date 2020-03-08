A, B = map(int, input().split())
C = (A + B) / 2
print(int(C) if C.is_integer() else 'IMPOSSIBLE')
