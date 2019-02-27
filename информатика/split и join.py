#23 4 62 -17 8 92 0 5 6 7
#a = input().split(' ')
#new_a = ' '.join(a)

#Дан список. Надо вывести наибольший элемент и его индекс

#a = input().split(' ')
#m = int(a[0])
#k = 0
#for i in range(len(a)):
#    if m < int(a[i]):
#        m = int(a[i])
#        k = i
#print(m, k)

#Вводится список ростов людей и рост Пети. Нужно вывести, под каким номером Петя
#должен встать в строй.

#a = input().split(' ')
#k = int(input())
#for i in range(len(a)):
#    if k > int(a[i]):
#        print(i)
#        break

#Дан список, упорядоченный по неубыванию. Вывести количество различных элементов

x = input().split(' ')
s = 1
for i in range(len(x) - 1):
    if int(x[i]) != int(x[i+1]):
        s += 1
print(s)
