#-Collect two inputs for father and son between the range of 1 - 80
#-Calculate the age difference by deducting the son's age from the father's age
#-Calculate the year the father will be twice as old his son
#-use the absolute value function to ensure the result is always positive
#-print result

father_age = int(input("Enter father's age (1-80): "))
son_age = int(input("Enter son's age (1-80): "))

age_difference = father_age - son_age

father_twice_old = age_difference - son_age

result = abs(father_twice_old)

print(f"Result: {result}")
