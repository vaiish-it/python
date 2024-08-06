#initialize list
lst = [10,20,50,40,49,79]

#initialize largest with first element
largest = lst[0]

#traverse the array
for i in lst:
    if i>largest:
        largest = i

print("largest number in list: ", largest)