#-Collect three integers
#-Assume 'a' is the largest to start
#-If 'b' is bigger, update to largest
#-If 'c' is bigger than the current bigger, update largest
#-Display result

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
    
print(f"Largest number: {largest}")
