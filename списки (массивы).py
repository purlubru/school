#l = input().split(' ')
#for i in l:
#    if int(i) % 2 == 0:
#        print(i)

l = input().split(' ')
for i in range(len(l)-1):
  if int(l[i])<int(l[i+1]):
      print(l[i+1])
