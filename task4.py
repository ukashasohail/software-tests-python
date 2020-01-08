input1 = input("enter first number: ")
input2 = input("enter second number: ")
input3 = input("enter third number: ")


def sorter(n1, n2, n3):

    arr = [n1, n2, n3]

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

try:
    n1 = int(input1)
    n2 = int(input2)
    n3 = int(input3)

    result = sorter(n1, n2, n3)

    print("sorted numbers are: ", result)

except:
    print("input valid value")
