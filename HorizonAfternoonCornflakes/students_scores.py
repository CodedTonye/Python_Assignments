#-Initialize pass count and fail count to zero
#-Loop 15 times to get 15 student's scores
#-prompt user input
#-Check if the student passes or failed
#-Display final results

pass_count = 0
fail_count = 0

for count in range(1, 16):
    score = float(input(f"Enter Student {count} score: "))
    
    if score >= 45:
        pass_count += 1
    else:
        fail_count += 1
        
print(f"\nStudents Passed: {pass_count}")
print(f"Students Failed: {fail_count}")
