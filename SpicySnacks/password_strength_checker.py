#-Collect user input
#-Get the number of characters
#-Check password strength based on length
#-Display the result

password = input("Enter your password to check strength: ")

length = len(password)

if length < 1:
    strength = "Invalid password (Too short)"
elif length < 6:
    strength = "Weak"
elif length <= 10:
    strength = "Medium"
else:
    strength = "Strong"
    
print(f"Password length: {length}")
print(f"Password strength: {strength}")
