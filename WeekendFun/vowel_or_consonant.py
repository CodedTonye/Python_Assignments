#-Get user input
#-Check if it's exactly one letter of the alphabet
#-Check if the letter is in the vowel list

char = input("Enter a single letter: ").lower().strip()

if len(char) != 1 or not char.isalpha():
    print("Invalid input")
else:
    if char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
