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
