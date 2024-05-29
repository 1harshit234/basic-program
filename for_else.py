#here direct use of the for and else;

"""for i in range(1,5):
    print(i)
else:
    print("harshit")

# here we used while and else:
i = 0 
while i<3:
    print(i)
    i = i+1
else:
    print("i ")"""


#method 3:
#here we wil use for with condition so that it may be break":
i = 7
while i >0 :
    print(i)
    i -=1
    if i == 4:
        break
    else:
        print("round 3",i)