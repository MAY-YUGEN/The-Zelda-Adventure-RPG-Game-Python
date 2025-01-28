print ("Program for printing number Assending and dessending Order")

firval = eval(input("Enter Starting Value: "))
print("Given Staring value is",firval)

secval = eval(input("Enter Ending Value: "))
print("Given Ending Value Is",secval)

ch=eval(input("Enter 1 For Assending Order And 2 For Dessending Order : "))
if(ch==1):    
    for i in range(firval,secval):       
        print(i)
        
elif(ch==2):
    for i in range(secval,firval,-1):        
        print(i)
else:
    print("Invalid Input")
    
