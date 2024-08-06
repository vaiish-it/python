count=0

#taking input from user 
string= input("Enter a String: ")
char= input ("Enter a character to count: ")

#using for loop and conditional statement to count the occurence of a character 
for i in string:
    if i==char:
        count+=1

    #Print the number of charcater occured 
        print (count)