arr = []

def sorter(arr):
	n = len(arr)

	for i in range(n):

		for j in range(0, n-i-1):

			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

try:
    input1 = int(input("enter number of array elements: "))


    for i in range(0,input1):

        input_number = int(input("enter a number: "))

        arr.append(input_number)

        sorter(arr)

    print ("Sorted array is: ", arr)
        
except:
    print("invalid input")
