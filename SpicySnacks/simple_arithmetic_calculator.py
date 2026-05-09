#-Get input from the user(first number, second number and operator)
#-Perform calculation based on the operator
#-print the result

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("Enter operator number: ")

if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    result = first_number / second_number
else:
    result = "Invalid operator!"
    
print(f"Result: {result}")
