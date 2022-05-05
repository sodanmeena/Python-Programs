def fibonacci(n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nterm = int(input("how many term: "))

if nterm <= 0:
    print("please enter a positive integer")

else:
    print("fibonacci sequence")
    for i in range(nterm):
        print(fibonacci(i))