#input string from user

string = input("Enter a string: ")

reversed_string = ""

#using for loop to reverse the string

for char in string:
    reversed_string = char + reversed_string  # Appending characters in reverse order

#print reversed string

print("Reversed string:", reversed_string)