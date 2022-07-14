def foo(x):
    """
    A test function for doctest module
    >>> foo(4)
    4
    >>> foo(5)
    5
    >>> foo(3)
    3
    
    """
    if x <= 3:
        return 0
    else:
        return x