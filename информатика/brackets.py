s = input()
br = []
for el in s:
    if el == '(':
        br.append(el)
    elif el == ')':
        if br == []:
            br.append('error')
            break
        else:
            x = br.pop()
if br == []:
    print('RIGHT')
else:
    print('ERROR')
