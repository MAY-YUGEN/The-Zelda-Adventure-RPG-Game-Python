print("Program for Printing Odd Number Only")

firval = eval(input("Enter Starting Value : "))
print("Starting Value is : ",firval)

secval = eval(input("Enter Last Value : "))
print("Last Value is : ",secval)

print("Odd Number are :")
for i in range(firval,secval):
    if(i % 2 == 1):
        print (i)


print("Even Number are :")
for i in range(firval,secval):
    if(i % 2 == 0):
        print(i)




