import math

x1 = int(input("write the number you want"))
y1 = int(input("write the number you want"))


x2 = int(input("write the number you want"))
y2 = int(input("write the number you want"))

x3 = int(input("write the number you want"))
y3 = int(input("write the number you want"))

print(f"the co ordinates of the triangles are{x1,y1},{x2,y2},{x3,y3}")
x = pow(x1-x2,2) + pow(y1-y2,2)
y = pow(x2-x3,2) + pow(y2-y3,2)
z = pow(x3-x1,2) + pow(y3-y1,2)
print(x,y,z)
                                      
if(x==y==z):
 area = (math.sqrt(3)/4)*pow(z,2)
 print("the area of the trriangle is ",area)
elif(x==y!=z or x!=y==z or y==z!=x):
  print(0.5*x*y)
else :
  print("we can do it by herons formula")
 

