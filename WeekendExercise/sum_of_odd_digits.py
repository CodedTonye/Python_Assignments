number = input("Enter a number: ")

odd_sum = 0

for char in number:
    digit = int(char)
    
    if digit % 2 != 0:
        odd_sum += digit
print(f"Sum of odd digits: {odd_sum}")
