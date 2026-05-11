number = int(input("Enter a number: "))
count = 0


for count in range(1, number + 1):
    if number % count == 0:
        count += 1
    
print(f"The number {number} has {count} divisors.")
       
