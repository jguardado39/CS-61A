# Question 1

from operator import add, sub

def a_plus_abs_b(a,b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub # sub(2, -3) = 2 - (-3) = 2 + 3
     else:
        f = add
    return f(a, b)



# Question 2

def two_of_three(a, b, c):
    """ Return x*x + y*y, where x and y are the two largest members of the
        positive numbers a, b, and c.

        >>> two_of_three(1, 2, 3):
        13
        >>> two_of_three(5, 3, 1):
        34
        >>> two_of_three(10, 2, 8):
        164
        >>> two_of_three(5, 5, 5):
        50
    """
    return sum(i*i for i in sorted([a, b, c]) [1:3])

# This is a bit more complicated but this just states that we will multiply the
# all of the sorted list and will only take the sum of the last two of the list
# in lue item 2 and item 3.

# Question 3

def largest_factor(n):
    """ Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factors is 1 and 13 since 13 is a prime number
    1
    """
    m = n - 1 # Start with the highest factor which could be n-1
    while n % m != 0 # while loop as long as n does not divide m
        m -= 1 # subtract 1 to m and continue the loop
    return m

# Question 4

def if_function(condition, true_result, false_result):
    """" Return true_result if condition is a true value, and
        false_result otherwise.

        >>> if_function(True, 2, 3)
        2
        >>> if_function(False, 2, 3)
        3
        >>> if_function(3 == 2, 3 + 2, 3 - 2)
        1
        >>> if_function(3 > 2, 3 + 2, 3 + 2, 3 - 2)
        5
        """"
        if condition:
            return true_result
        else:
            return false_result

def with_if_statement():
    """"
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True
def t():
    return 1
def f():
    return None #returns nothing

# Question 5

def hailstone(n):
    """ Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
  count = 1 # need counter for the labeling of hailstone
    while n >= 1:
      print (n) # prints initial n

      if n == 1:
        return count #this stops the the counter
      elif  n % 2 == 0:
        n = n // 2 # for astetic purposes to create integers
      else:
        n = 3 * n + 1

      count += 1 # adding count every time it loops
#test
