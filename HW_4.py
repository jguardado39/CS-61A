# Question 1 : Taxicab Distance
def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function.""""
    return (st + ave) * (st + ave + 1) // 2 + ave

def street (inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int((8 * z + 1) ** 0.5 - 1) / 2)

def taxicab(a,b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46,7)
    >>> ess_a_bagel = intersection(51,3)
    >>> taxicab(times_square,ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a)-street(b)) + abs(avenue(a)-avenue(b))
    # abs(w(a)-avenue(a)-w(b)-avenue(b)) - abs(a-(w(a)**2+w(a)//2)-b-(w(b)**2+w(b)//2))

# Question 2: Squares only
def sqaures(s):
    """Returns a new list containing sqaure roots of the elements of the
    original list that are percect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """

# Question 3: G function
G(n) = n, if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3)

def g(n):
    """Return the value of G(n), computed recursively

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check (HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n in (1, 2, 3):
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3) # Just the recursion that we
                                                  # used for the function

def g_iter(n):
    """ Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2 * b + 3 * a
        n = n - 1
    return c

# Question 4: Ping Pong

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def pingpong_next(k, p, up):
        if k == n: # This will terminate the funciton
            return p
        if up:
            return pingpong_switch(k + 1, p + 1, up)
        else:
            return pingpong_switch(k + 1, p - 1, up) # Initial when not up

    def pingpong_switch(k, p, up):
        if k % 7 == 0 or has_seven(k): # Either has 7 or is a multiple of 7
            return pingpong_next(k, p, not up)
        else:
            return pingpong_next(k, p, up)

    return pingpong_next(1, 1, True) # This is to inititate pingpong_next

def has_seven(k):
  """Returns True if at least one of the digits of k is a 7, False otherwise.

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
  if k % 10 == 7:
    return True
  elif k < 10:
    return False
  else:
    return has_seven(k // 10)

# Question 5: Count change

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    
