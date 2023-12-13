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

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def total_wins():
    """
    -------------------------------------------------------
    Takes no parameters and prompts the user to enter a series of strings representing game outcomes.
    The user should enter an empty string to signal the end of the series. 
    Counts occurrences of "purple" and "gold" in the input strings and returns the count for each.
    Use: purple_count, gold_count = total_wins()
    -------------------------------------------------------
    Returns:
        purple_count - number of times "purple" appeared in the input (int)
        gold_count - number of times "gold" appeared in the input (int)
    ------------------------------------------------------
    """

    purple_count = 0
    gold_count = 0
    user_input = input("Enter the winning team: ")

    while user_input != "":
        if user_input == "purple":
            purple_count += 1
        elif user_input == "gold":
            gold_count += 1
        user_input = input("Enter the winning team: ")

    return int(purple_count), int(gold_count)


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    if number <= 1:
        is_prime = False
    else:
        divisor = 2
        is_prime = True

        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

    return is_prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    month = 1
    balance = principal_amount

    while balance > 0:
        monthly_interest = (interest_rate / 100) / 12 * balance
        if balance < payment:
            payment = balance + monthly_interest
            balance = 0
        else:
            balance -= payment - monthly_interest
        print(f"{month:4d} {monthly_interest:8.2f} {payment:9.2f} {balance:9.2f}")
        month += 1

    return None


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """

    digits = 0
    num = abs(number)

    while num != 0:
        num //= 10
        digits += 1

    return int(digits)


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """

    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    return int(total)
