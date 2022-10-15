a = int(input("enter a: "))
b = int(input("enter b: "))

s = ((a % b) * (b % a)) + 1
print(s)