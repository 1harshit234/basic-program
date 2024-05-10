#taking the input from the user
x = int(input("write the number "))
y = int(input("write the number "))
z = int(input("write the number "))
#comparsion between the numbers 
if ( x>y and y>z):
  print(f"the largest among them is {x} followed by {y} and then {z}")
elif(y>x and x>z):
  print(f"the largest numbers among the three is {y} followed by {x} and then {z}")
elif(z>x and x>y):
  print(f"the largest among the three is {z} followed by {x} and then {y} ")
elif(x>z and z>y):
  print(f"the largest among them is {x} followed by {z} then {y}")
elif(y>z and z>x):
  print(f"the largest among them is {y} followed by {z} then {x}")
else:
  print(f"the largest is {z} followed by {y} and then {x}")
 