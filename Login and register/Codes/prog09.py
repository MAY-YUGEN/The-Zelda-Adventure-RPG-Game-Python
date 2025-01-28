print("Program for Removing the Dublicate value and Create Unique Value List")


list1 = [10,10,11,11,12,12,13,13,14,14]
print("Total all Number in the List:",list1)
list2 = []

for a in list1:
    if a not in list2:
        list2.append(a)
    
print(list2)
