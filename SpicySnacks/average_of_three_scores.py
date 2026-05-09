#-Collect three scores from user
#-Calculate the average
#-Determine the letter grade based on the average
#-Display the results

score_one = float(input("Enter first score: "))
score_two = float(input("Enter second score: "))
score_three = float(input("Enter third score: "))

average = (score_one + score_two + score_three) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
    
print(f"Average Score: {average:.2f}")
print(f"Letter Grade: {grade}")
