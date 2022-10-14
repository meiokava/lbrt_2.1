y = float(input('enter angle of the clock: '))
# 1 hour = 30 degree, 1 minute = 0.5 degree, 1 second = 0.083 degree
#degree is solved as (h * 30) + (m * 0.5) + (s * 0.083)

h = y // 30 
m = (y % 30) // 0.5
s = ((y % 30) % 0.5) // 0.083
sol = (m*6) + (s*0.1)
print('angle for minutes is: ', sol, ' full hours: ', h, 'full minutes: ', m)