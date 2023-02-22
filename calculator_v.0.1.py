print("Welcome to Lukas' calculator!")
def calculator():
    operation = input("Would you like to add, subtract, multiply, or divide?: ")
    operation = operation.upper()
    int_1 = input("What is the first integer you would like to input?: ")
    int_1 = int(int_1)
    int_2 = input("What is the second integer you would like to input?: ")
    int_2 = int(int_2)
    if operation == "ADD":
        print(int_1+int_2)
    if operation == "SUBTRACT":
        print(int_1-int_2)
    if operation == "MULTIPLY":
        print(int_1*int_2)
    if operation == "DIVIDE":
        print(int_1/int_2)
    else:
        print("I can't accept that input")
calculator()
print("Thank you for using Lukas' calculator")
