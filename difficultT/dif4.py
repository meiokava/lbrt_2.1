k = int(input("Enter k (1<= k <= 180): "))

if (k%2 == 0):
    n1 = k // 2
    n2 = n1 + 9
    n3 = n2 % 10
if (k%2 != 0):
    n1 = k//2 + 1
    n2 = n1 + 9
    n3 = n2 // 10
print("pair number is: ",n1,"\ndigit with k is: ",n2,"\ndigit k is: ",n3)