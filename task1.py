input1 = input("enter first number: ")
input2 = input("enter second number: ")
input3 = input("enter third number: ")

def largest(n1, n2, n3):
    
    if (n1 >= n2 and n1 >= n3):
        return n1

    elif (n2 >= n1 and n2 >= n3):
        return n2

    elif (n3 >= n1 and n3 >= n2):
        return n3
        
try:
    n1 = int(input1)
    n2 = int(input2)
    n3 = int(input3)

    result = largest(n1, n2, n3)

    print("largst number is: ", result)

except:
    print("input valid value")


