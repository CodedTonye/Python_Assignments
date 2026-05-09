#-Get number from user input
#-Loop from 1 to the input number
#-Multiply the "*" by row numbers
#-Display result

number = int(input("Enter number: "))

for row in range(1, number + 1):
    print("* " * row)
