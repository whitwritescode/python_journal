# Define a function for each operation
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error: Division by zero is not allowed"
  return x / y

# Define a main function for the calculator
def calculator():
  print("Simple Calculator")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")

  choice = input("Enter your choice (1/2/3/4): ")

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

  elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

  elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

  elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
  else:
    print("Invalid choice")

# Call the main function
calculator()
