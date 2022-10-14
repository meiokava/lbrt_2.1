y = float(input('enter degree of the clock: '))
# hour = 30 degree, 1 minute = 0.5 degree, 1second = 0.083 degree

h = y // 30
m = (y % 30) // 0.5
s = ((y % 30) % 0.5) // 0.083
print('hours: ', h, 'minutes: ', m, 'seconds: ', s)