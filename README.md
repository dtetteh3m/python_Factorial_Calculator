# python_Factorial_Calculator
This simple Python program calculates the factorial of a given number entered by the user
Factorial Calculator in Python
This simple Python program calculates the factorial of a given number entered by the user.
It demonstrates basic concepts of:

Functions
Loops (for loop)
User input validation
How It Works
The user is prompted to enter a number.
The program checks if the input is a valid integer.
If valid:
The program calculates the factorial of the number using a loop.
Displays the result.
If invalid (non-numeric or negative):
Displays an appropriate error message.

##Code Example
def calculate_number_factor(num):
    try:
        num = int(num)
        if num < 0:
            return "Error: Factorial of negative numbers is undefined."
        initial = 1
        for i in range(1, num + 1):
            initial *= i
        return initial
    except ValueError:
        return "Error: Please enter a valid number."

num = input("Enter a number: ")
print(f"The factorial of {num} is {calculate_number_factor(num)}")
