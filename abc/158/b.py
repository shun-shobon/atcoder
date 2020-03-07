N, A, B = map(int, input().split())
C = A + B
D = N // C
E = N % C
print(D * A + (A if A <= E else E))
