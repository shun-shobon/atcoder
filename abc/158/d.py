from collections import deque
S = deque(input())
Q = int(input())
query = [input().split() for _ in range(Q)]
reverse = False
for q in query:
    if q[0] == '1':
        reverse = not reverse
    else:
        if q[1] == '1':
            S.append(q[2]) if reverse else S.appendleft(q[2])
        else:
            S.appendleft(q[2]) if reverse else S.append(q[2])
if reverse:
    S.reverse()
print(''.join(S))
