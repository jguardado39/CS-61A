def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

# Question 1

def product (n, term):
    """ Return the product of the first n term in a sequence.

    n -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square) # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square) #1^2 2^2 * 3^2 * 4^2 * 5^2
    14400
    """

    i, s  = 1, 1 # Counter and total
    while i <= n: # stop iff i > n
        s = term(i) * s
        i += 1
    return s # Return total

# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial (n):
    """ Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from costrcut_check import check
    >>> chekc(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    return product(n, identity) # Using the function product with the lambda
                                # funciton and input n

# Question 2
def make_adder(n):
    """ Return a function that takes an argument K and returns N + K

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    return lambda k: n + k
