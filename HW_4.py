def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function.""""
    return (st + ave) * (st + ave + 1) // 2 + ave

def street (inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2
