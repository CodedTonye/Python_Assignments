#-Check if a number is prime.
#-Check divisibility up to the square root of number for efficiency.
#-Check if a number reads the same forward and backward.
#-Returns True if number is both prime and a palindrome.
  
def is_prime(number):
    if number < 2:
        return False
    
    for count in range(2, int(n**0.5) + 1):
        if number % count == 0:
            return False
    return True

def is_palindrome(number):
    original = str(number)
    reversed_str = ""
    
    for char in original:
        reversed_str = char + reversed_str
    return original == reversed_str

def is_prime_palindrome(number):
    return is_palindrome(number) and is_prime(number)

