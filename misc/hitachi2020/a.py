S = input()
ans = False
for i in range(1, 6):
    if S == 'hi' * i:
        ans = True
        break
print('Yes' if ans else 'No')
