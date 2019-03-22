n = int(input())
a = 0
k = []
while a != n - 1:
    p = int(input())
    a += 1
    k.append(p)
u = sorted(k)
u.append(0)
t = 1
e = []
while t != n + 1:
    e.append(t)
    t += 1
for i in range(n):
    if u[i] != e[i]:
        print(i + 1)
        break
