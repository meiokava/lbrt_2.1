h = int(input('enter hours: '))
m = int(input('enter minutes: '))
s = int(input('enter seconds: '))
# hour = 30 degree, 1 minute = 0.5 degree, 1second = 0.083 degree

dg = (h * 30) + (m * 0.5) + (s * 0.083)
print('angle is equal: ', dg)