# Factorial Calculator in Python

This simple Python program calculates the factorial of a given number entered by the user.  
It demonstrates basic concepts of:
- Functions
- Loops (`for` loop)
- Error handling with `try` / `except`
- User input validation

---

## How It Works

1. The user is prompted to enter a number.
2. The program checks if the input is a valid integer.
3. If valid:
   - The program calculates the factorial of the number using a loop.
   - Displays the result.
4. If invalid (non-numeric or negative):
   - Displays an appropriate error message.

---

## Code Example

```python
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
