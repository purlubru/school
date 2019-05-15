n = int(input())
min = -1
for i in range(n):
    k = int(input())
    if k%7 == 0:
        if min == -1:
            min = k
        else:
            if k < min:
                min = k
print(min)
        
