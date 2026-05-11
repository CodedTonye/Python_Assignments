count = 0

for number in range(2, 101):
    is_prime = True
    
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            is_prime = False
            break
            
    if is_prime:
        count += 1
      
print(f"There are {count} prime numbers between 1 and 100.")
