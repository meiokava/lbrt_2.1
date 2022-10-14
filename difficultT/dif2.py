a1 = int(input('enter a1: '))
a2 = int (input('enter a2: '))
b1 = int(input('enter b1: '))
b2 = int(input('enter b2: '))

res1 = a2 + b2 + (a1+b1) // 10
res2 = (a1 + b1) % 10
print(res1, res2)