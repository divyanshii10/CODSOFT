print("\n----Welcome to my mini Project 'Calculator'----\n")

operation = input("Enter the operation you want to perform:\n")

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if(operation == "+"):
    print(f'The sum of {a} and {b} is',a+b)
elif(operation == "-"):
     print(f'The difference of {a} and {b} is',a-b)
elif(operation == "%"):
    print(f'The modulus of {a} and {b} is',a%b)
elif(operation == "/"):
    print(f'The division of {a} and {b} is',a//b)
elif(operation == "*"):
    print(f'The multiplication of {a} and {b} is',a*b)
else:
    print("Please enter a valid operation!")
