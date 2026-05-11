number = input("Enter a number: ")

even_sum = 0

for char in number:
    digit = int(char)
    
    if digit % 2 == 0:
        even_sum += digit
print(f"Sum of even digits: {even_sum}")
