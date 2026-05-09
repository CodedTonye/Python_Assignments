from unittest import TestCase

import palindrome_and_prime_numbers_function

class TestPrimePalindrome(TestCase):
    
    def test_valid_prime_palindromes(self):
        self.assertTrue(palindrome_and_prime_numbers_function.is_prime_palindrome(11))
        self.assertTrue(palindrome_and_prime_numbers_function.is_prime_palindrome(131))
        self.assertTrue(palindrome_and_prime_numbers_function.is_prime_palindrome(2)) 
        
    def test_prime_but_not_palindrome(self):
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(13))
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(19))
        
    def test_palindrome_but_not_prime(self):
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(9))
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(22))
        
    def test_edge_cases(self):
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(0))
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(1))
        self.assertFalse(palindrome_and_prime_numbers_function.is_prime_palindrome(-11)) 
