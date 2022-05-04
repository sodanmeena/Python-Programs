value = input("Enter the value to check palindrome: ")

revval = value[::-1]

if value == revval :
    print("yes it is palindrome")

else:
    print("no it is not a palindrome")