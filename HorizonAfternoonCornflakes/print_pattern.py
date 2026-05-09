#-Use outer loop to count from 5 down to 1
#-Use inner loop to count down from outter loop number to 1
#-Display result
#-Move to the next line after each row

for row in range(5, 0, -1):
    for count in range(row, 0, -1):
        print(count, end=" ")
        
    print()
