text = "Welcome to Semicolon Africa."
count = 0

for char in text:
    if char.islower():
        count += 1
print(f"Number of uppercase letters: {count}")
