def multiplication_or_sum(num1,num2):
    
    product= num1*num2
    #cheking if the product is less then 1000
    if product  <= 1000:
        return product
    else:
        #if product greter then 1000 so calculate sum 
        return num1 + num2
    
#giving Condition 1        
result1 = multiplication_or_sum(20,30)
print("First Result Is :",result1)

#giving Condition 2
result2 = multiplication_or_sum(40,30)
print("Second Result is :",result2)