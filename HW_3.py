# Question 1
def has_seven(k):
    """ Returns True if at least one of the digits of k is a 7, False otherwise

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    while k > 0:
      last, k = k % 10, k // 10
      if last == 7:
        return True
    return False

# Another code to answer this quesiton
    # if k % 10 == 7:
    #     return True
    # elif k < 10:
    #     return False
    # else:
    #     return has_seven(k // 10)

# Question 2
def summation(n, term):
    """ Return the sum of the first n terms in the seqence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2 ** x) # 2^`1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> form construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n -1, term)

# Another way to answer this question (w/ while loop)
    # i, s  = 1, 0
    # while i <= n:
    #     s = term(i) + s
    #     i += 1
    # return s

# Question 3

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

from operator import add, mul

def accumulate(combiner, base, n, term):
    """" Return the result of combining the first n terms in a swquence and base
    The terms to be combined are term(1), term(2), ..., term(n). Combiner is a
    two-argument commtative function.

    >>> accumulate(add, 0, 5, identity) # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11, 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square) # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square) # 2 * 1^2 * 2^2 * 3^2
    72
    """
    if n == 0:
        return base
    else:
        return combiner(term(n-1))
