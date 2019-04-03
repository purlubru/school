#def fact(x):
#    a = 1
#    while x > 1:
#        a = x * a
#        x = x - 1
#    return a

#def main():
#    n = int(input())
#    m = int(input())
#    print(fact(n), fact(m))

#main()

#from math import sqrt

#def distance(x1, y1, x2, y2):
#    return sqrt((x1-x2)**2 +(y1-y2)**2)

#def main():
#    x1 = float(input())
#    y1 = float(input())
#    x2 = float(input())
#    y2 = float(input())
#    print(distance(x1, y1, x2, y2))

#main()
    
def power(a, n):
    new = 1
    for i in range(n):
        new=new*a
    return(new)    
def main():
    a=float(input())
    n=int(input())
    print(power(a, n))
main()

