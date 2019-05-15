def maximum(a):
    m = int(a[0])
    for i in range(1, len(a)):
        if m < int(a[i]):
            m = int(a[i])
    return m

def main():
    hfx = input().split(' ')
    print(maximum(hfx))

main()
