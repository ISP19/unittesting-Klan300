def average( lst ):
    if len(lst) == 0:
        raise ValueError
    return sum(lst)/len(lst)