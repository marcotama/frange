from fractions import Fraction

def frange(start, stop, jump, end=False, via_str=False):
    """
    Equivalent of Python 3 range for decimal numbers.
    
    Notice that, because of arithmetic errors, it is safest to
    pass the arguments as strings, so they can be interpreted to exact fractions.
    
    >>> assert Fraction('1.1') - Fraction(11, 10) == 0.0
    >>> assert Fraction( 0.1 ) - Fraction(1, 10) == Fraction(1, 180143985094819840)
    
    Parameter `via_str` can be set to True to transform inputs in strings and then to fractions.
    When inputs are all non-periodic (in base 10), even if decimal, this method is safe as long
    as approximation happens beyond the decimal digits that Python uses for printing.
    
    
    For example, in the case of 0.1, this is the case:
    
    >>> assert str(0.1) == '0.1'
    >>> assert '%.50f' % 0.1 == '0.10000000000000000555111512312578270211815834045410'
    
    
    If you are not sure whether your decimal inputs all have this property, you are better off
    passing them as strings. String representations can be in integer, decimal, exponential or
    even fraction notation.
    
    >>> assert list(frange(1, 100.0, '0.1', end=True))[-1] == 100.0
    >>> assert list(frange(1.0, '100', '1/10', end=True))[-1] == 100.0
    >>> assert list(frange('1', '100.0', '.1', end=True))[-1] == 100.0
    >>> assert list(frange('1.0', 100, '1e-1', end=True))[-1] == 100.0
    >>> assert list(frange(1, 100.0, 0.1, end=True))[-1] != 100.0
    >>> assert list(frange(1, 100.0, 0.1, end=True, via_str=True))[-1] == 100.0

    """
    if float(jump) == 0:
        raise ValueError('frange() arg 3 must not be zero')
    if stop is None:
      start, stop = 0, start
    if via_str:
        start = str(start)
        stop = str(stop)
        jump = str(jump)
    start = Fraction(start)
    stop = Fraction(stop)
    jump = Fraction(jump)
    if jump < 0:
        for i in frange(-start, -stop, -jump, end=end, via_str=False):
            yield -i
    else:
        while start < stop:
            yield float(start)
            start += jump
        if end and start == stop:
            yield(float(start))


if __name__ == '__main__':
    assert Fraction('1.1') - Fraction(11, 10) == 0.0
    assert Fraction( 0.1 ) - Fraction(1, 10) == Fraction(1, 180143985094819840)
    
    assert str(0.1) == '0.1'
    assert '%.50f' % 0.1 == '0.10000000000000000555111512312578270211815834045410'
    
    assert list(frange(1, 100.0, '0.1', end=True))[-1] == 100.0
    assert list(frange(1.0, '100', '1/10', end=True))[-1] == 100.0
    assert list(frange('1', '100.0', '.1', end=True))[-1] == 100.0
    assert list(frange('1.0', 100, '1e-1', end=True))[-1] == 100.0
    assert list(frange(1, 100.0, 0.1, end=True))[-1] != 100.0
    assert list(frange(1, 100.0, 0.1, end=True, via_str=True))[-1] == 100.0

    assert list(frange(2, 3, '1/6', end=True))[-1] == 3.0
    assert list(frange(0, 100, '1/3', end=True))[-1] == 100.0
    assert list(frange(4, jump=.11))[-1] == 3.96
    assert list(frange(4, 0, -0.1, via_str=True))[-1] == 0.1
