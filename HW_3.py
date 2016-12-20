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

# This is the same concept as Quiz 1 but instead of looking for unique digits,
# we are looking for a 7 in any digit.


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
        return term(n) + summation(n - 1, term)

# Another way to answer this question (w/ while loop)
    # i, s  = 1, 0
    # while i <= n:
    #     s = term(i) + s
    #     i += 1
    # return s

# This is just a basic while look where it adds all the numbers that need to be
# added

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
    return combiner(term(n), accumulate(combiner, base, n - 1, term))
# This is a simple if statement where we use recurssion in order to get accumulate
# to zero and adds/multiplies everything else

def summation_using_accumulate(n,term):
    """ Returns the sum of term(1) + ... + term(n). The implementation uses
    accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recurssion', 'For', 'While'])
    True
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """ An implementation of product using accumulate

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate'
    ...       ['Recurssion', 'For', 'While'])
    True
    """
    return accumulate(mul, 1, n, term)

# Using accumulate we can specify the summation or product so creating the fucntion
# first we can make simplier function that specify other sub-functions.

# Question 4
def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate PRED. COMBINER is a two-argument function.
    If v1, v2, ..., vk are the values in TERM(1), TERM(2), ..., TREM(N)
    that statisfy PRED, then the result is
        BASE COMBINER v1 COMBINER v2 ... COMBINER vk
    (treating COMBINER as if it were a binary operator, like +). The
    implemenation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity) # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add 0, odd, 5, identity) # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square) # 1 * 9 * 16 * 25
    3600
    >>> # Do not use while/for loop or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion'])
    True
    """
    def combine_if(x,y):
        if pred(y):
            return combiner(x, y)
        else:
        return x
    return accumulate(combine_if, base, n, term)

def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

# Question 5
def repeated(f, n):
    """ Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    """
    while n > 0:
        if n == 0:
            return 1
        return repeated(f, n - 1)
