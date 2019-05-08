def put_in(stack, m):
    n = len(stack)
    b = [0] * (n+1)
    for i in range(n):
        b[i] = stack[i] #заполняем массив b значениями из массива stack
    b[-1] = m #кладём в дополнительную ячейку новое число, которое ввёл пользователь
    return b

def put_out(stack):
    n = stack[0]
    b = stack[1:]
    return b, n

def main():
    stack = []
    s = input()
    while s != 'red':
        if s == 'push':
            n = int(input('Введите число: '))
            stack = put_in(stack, n) #вместо этого можно просто написать stack.append(n)
            print(stack)
        elif s == 'pop':
            stack, n = put_out(stack) #вместо этого можно просто написать n = stack.pop()
            print(n)
        else:
            print('error')
        s = input()

main()
