print('''
 _____________________
|  _________________  |
| | Hi           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

def calculator(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '/':
        if b == 0:
            print("Divison by Zero is not possible.")
        else:
            return a/b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a*b
    else:
        print("Invalid Operation")
        raise ValueError("This operation is not defined for Calculator.")

calculation = True
f_number = None
while calculation:
    
    if f_number is None:
        f_number = float(input("Enter the first number:\n"))


    # f_number = float(input("Enter first number:\n"))
    operation = input("*\n+\n-\n/\nChoose an operation:\n")
    s_number = float(input("Enter second number:\n"))
    
    #Print the result of the calculator after each operation
    result = calculator(a=f_number,b=s_number,operation=operation)
    print(f"Result:{result}")

    restart = input(f"Type 'y' if you want to continue the calculation with {result} else Type 'n'.").lower()
    if restart == "y":
        f_number = result
        
    elif restart == "n":
        calculation = True
        f_number = None
        print("\n"*100)
        print('''
 _____________________
|  _________________  |
| | Hi           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')
    else:
        print("Invalid Input.Enter 'y' or 'n'.")
        calculation = False
        
# print(calculator(f_number,s_number,operation))
#you have to keep the function inside the loop if you want to execute the code repeatedly
