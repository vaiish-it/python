# sum of elements

def sumlist(list):
    sum=0
    for i in range(len(list)):
        sum = sum+list[i]
    return sum

#initialise list
list = [11, 15, 9, 0, 8, 2]
print(list)
print("sum of list: ",sumlist(list))