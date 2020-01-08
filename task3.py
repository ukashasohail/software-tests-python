import math 

input1 = input("enter number: ")

try:
    n1 = float(input1)

    result = math.sqrt(n1)

    print(result)

except:
    print("invalid input")
