a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
d = int(input("enter d: "))

if (a < b):
    if (c > d):
        x = 1

    elif (c == d):
        x = 2
    
    else:
        x = 3

elif (a == b):
    x = 4

elif (c == d):
    x = 5

else:
    x = 6

print(x)
