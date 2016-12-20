# Question 1
def multiple(a, b):
    """ Return the smallest number n that is a multiple of both a and b

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    c = min(a ,b)
    while True: # whlie this statement is True
        if c % a == 0: and c % b == 0: # stops iff c is both divisible by a and b
            return c
        c += 1


# Question 2
def unique_digits(n):
    """ Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    unique = 0
    i = 0
    while i < 10:
        if has_digit(n, i):
            unique += 1
        i += 1
    return unique
# Using the has digit function  to find out wheter or not the number has different
# number of unique digits

def has_digit(n,k):
    while n > 0:
        last, n = n % 10, n // 10
        if last == k:
            return True
    return False
# This is a function that intakes a number and a digit and outputs True or False
# Depending on whether that digit is in that number.
