a = input().split(' ')
for j in range(len(a)):
    for i in range(len(a) - 1):
        if int(a[i]) > int(a[i+1]):
            p = a[i]
            a[i] = a[i+1]
            a[i+1] = p
print(a)
