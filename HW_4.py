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
    
