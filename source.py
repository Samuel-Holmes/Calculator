# Simple Calculator Programme 


# Setting the boolean for the while loop of the programme 

running = True

print("Hello welcome to the calculator if you would like to exit at any time then please enter 'n'")

# opening the loop 

while running:
    

    
    # programme needs to take user input and an operand 

    num1 = input("Please enter the first number: ")
    
    if num1 == 'n':
        break
    
    else:
        num2 = input("Please enter the second number: ")


    num1 = int(num1)
    num2 = int(num2)

    operand = input("Please enter the operand you require (*, /, +, -): ")

    # basic input taken now needs the conditional logic implemented

    if operand =="*":
        print(f"The answer is: {num1 * num2}")
    
    if operand == '/':
        print(f"The answer is: {num1 / num2}")

    if operand == '+':
        print(f"The answer is: {num1 + num2}")

    if operand == '-':
        print(f"The answer is: {num1 - num2}")

    