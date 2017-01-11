# Question 1: Replace Leaf

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if is_leaf(t) and root(t) == old:
        return tree(new)
    else:
        bs = [replace_leaf(b, old, new) for b in branches(t)]
        return tree(root(t), bs)

# Question 2: Swap
def swap(a,b):
    """ Swap the content of lists a and b

    >>> a = [1, 'two', 3]
    >>> b = [4, [5, 6]]
    >>> swap(a, b)
    >>> a
    [4, [5, 6]]
    >>> b
    [1, 'two', 3]
    """
    a[:], b[:] = list(a), list(b)

# Required Questions
# Question 3: Towers of Hanoi

def print_move (origin, destination):
    """Print instructions to move a disk."""
    print ("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are excatly three poles and start and end must be differnt. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start, end)
    else:
        other = 6 - start - end
        move_stack(n - 1, start, other)
        print_move(start, end)
        move_stack(n - 1, other, end)

# Interval

def str_interval(x):
    """Return a string reprsentation of interval x."""
    return '(0) to (1)'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an intervavl that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def interval(a,b):
    """ Construct an interval from a to b."""
    assert a <= b
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]
def upper_bound(x):
    """Return the uppower bound of intervval x."""
    return x[1]
def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = x[0] * y[0]
    p2 = x[0] * y[1]
    p3 = x[1] * y[0]
    p4 = x[1] * y[1]
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]

# Question 5: Sub Interval

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    negative_y = interval(-upper_bound(y), -lower_bound(y))
    return add_interval(x, negative_y)


# Question 6: Div Interval
def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any vvalue in y. Division is implemented as the mulitiplication of x by the
    reciprocal of y. """
    assert not (lower_bound(y) <= 0 <= upper_bound(y)) # Cannot divide by zero
    reciprocal_y = interval(1 / upper_bound(y), 1 / lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Question 7: Par Diff

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_part()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 2)
    r2 = interval(3, 4)
    return r1, r2

# Question 8: Multiple References

def multiple_references_explanation():
    return """The multiple reference problem exists.  The true value
    within a particular interval is fixed (though unknown).  Nested
    combinations that refer to the same interval twice may assume two different
    true values for the same interval, which is an error that results in
    intervals that are larger than they should be.

    Consider the case of i * i, where i is an interval from -1 to 1.  No value
    within this interval, when squared, will give a negative result.  However,
    our mul_interval function will allow us to choose 1 from the first
    reference to i and -1 from the second, giving an erroneous lower bound of
    -1.

    Hence, a program like par2 is better than par1 because it never combines
    the same interval more than once.
    """
# Question 9: Quadratic

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    extremum = -b / (2*a)
    f = lambda x: a * x * x + b * x + c
    l, u, e = map(f, (lower_bound(x), upper_bound(x), extremum))
    if extremum >= lower_bound(x) and extremum <= upper_bound(x):
        return interval(min(l, u, e), max(l, u, e))
    else:
        return interval(min(l, u), max(l, u))
