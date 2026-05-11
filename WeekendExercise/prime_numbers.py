for number in range(2, 101):
    for count in range(2, int(number**0.5) + 1):
        if number % count == 0:
            break
    else:
        print(number, end=" ")
    
