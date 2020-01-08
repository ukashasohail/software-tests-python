input1 = input("enter first number: ")
input2 = input("enter second number: ")

def compute_lcm(x, y):
       # choose the greater number

   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm


        
try:
    n1 = int(input1)
    n2 = int(input2)

    if n1 < 0 or n2 < 0:
        print("invalid input")

    else:
        print("The L.C.M. is", compute_lcm(n1, n2))


except:
    print("input valid value")

