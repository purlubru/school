l = input().split(' ')
for i in range(len(l)-1):
    if int(l[i]) * int(l[i+1]) > 0:
        print(l[i], l[i+1])
        break
