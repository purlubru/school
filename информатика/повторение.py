#n = int(input())
#a = 1
#i = 1
#while n != 0:
#    if i % 3 == 0:
#        a = a * n
#    n = int(input())
#    i += 1
#print(a)

#s = input()
#print(s.count(input())/len(s))

from math import sqrt

n = int(input())
a = 0
while n != 0:
    a = a + n * n
    n = int(input())
print(sqrt(a))
