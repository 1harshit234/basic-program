#taking the input from the user
x = int(input("write the numbers you want"))
if(x<0):
 print(f"write the numbers which is greater than 1")
elif(x == 0 or x ==1):
 print(f"the number {x} is not a prime numbers")
elif(x ==2):
  print(f"the given number {x} is a prime numbers")
else:
    for i in range(2,x):
     if x%i==0:
       print(f"the given number {x} is not a prime numbers")
       break
       
     else:
       print(f"the given numbers {x} is a prime numbers")
       break

 
