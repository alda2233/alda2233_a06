"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import detect_prime
# Constants

user_number = int(input("Enter a number to check for primality: "))
result = detect_prime(user_number)
print(result)
