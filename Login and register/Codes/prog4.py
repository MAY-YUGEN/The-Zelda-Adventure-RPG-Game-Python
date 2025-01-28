print ("Simple calculater")

firstval = eval(input("Enter First value :"))
print("Given First Value is :",firstval)

secondval = eval(input("Enter Second value :"))
print("Given Second Value is :",secondval)

print("Enter 1 for Addition , 2 for Subtraction, 3 for Maltiplication, 4 for Divition")
ch=eval(input("enter your Choice : "))
if(ch==1):
    print(firstval+secondval)
elif(ch==2):
    print(firstval-secondval)
elif(ch==3):
    print(firstval*secondval)
elif(ch==4):
    print(firstval/secondval)
else:
    print("Invalid Input")
