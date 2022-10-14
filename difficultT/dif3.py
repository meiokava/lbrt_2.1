a1 = int(input('enter a1: '))
a2 = int(input('enter a2: '))
a3 = int(input('enter a3: '))
b1 = int(input('enter b1: '))
b2 = int(input('enter b2: '))
b3= int(input('enter b3: '))

res1 = (a1 + b1) % 10
res2 = (a2 + b2 + (a1 + b1) // 10) % 10
res3 = a3+b3 + ((a2+b2) + (a1+b1) // 10) // 10
print(res1, res2, res3)