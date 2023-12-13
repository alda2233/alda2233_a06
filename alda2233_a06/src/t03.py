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
from functions import interest_table
# Constants

principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))
payment = float(input("Enter the monthly payment: "))

interest_table(principal, interest_rate, payment)
