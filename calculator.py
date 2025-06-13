def add(x, y): 
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
    
print("Welcome to the Calculator!")
print("7\t8\t9\t/\n4\t5\t6\t*\n1\t2\t3\t-\n0\t.\t=\t+")
print("Available operations: +  -  *  /")
while True:
    choice = input("Enter operation (+, -, *, /): ")
    if choice in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue
        if choice == '+':
            print("Result:", add(num1, num2))
        elif choice == '-':
            print("Result:", subtract(num1, num2))
        elif choice == '*':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid operator! Please use +, -, *, or /")
    next_calc = input("Do you want to perform another calculation? (yes/no): ")
    if next_calc.lower() not in ['yes', 'ye', 'y']:
        print("Thank you for using the calculator!")
        break