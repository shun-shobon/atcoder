S = sorted(input())
print('Yes' if S.count(S[0]) == 2 and S.count(S[2]) == 2 else 'No')
