Equivalent of Python 3 `range`, but allows the use of decimal numbers.


Usage:
```
> list(frange(0.0, 3.0, 0.5))
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
```

Since computers encode numbers in binary, those that are not perfectly
convertible in base 2 can create problems. For example:
```
> list(frange(0.0, 1.0, 0.1))
[0.0,
 0.1,
 0.2,
 0.30000000000000004,
 0.4,
 0.5,
 0.6000000000000001,
 0.7000000000000001,
 0.8,
 0.9]
```

To solve this problem, `frange` offers two approaches:

- to pass the numbers as strings or
- to pass them as floats and to set the `via_str` parameter to `True`

Examples:
```
> list(frange(1, 2.0, 0.1, end=True))
[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9000000000000001]
> list(frange(1, 2.0, '0.1', end=True))
[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
> list(frange(1.0, '2', '1/10', end=True))
[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
> list(frange('1', '2.0', '.1', end=True))
[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
> list(frange('1.0', 2, '1e-1', end=True))
[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
> list(frange(1, 2.0, 0.1, end=True, via_str=True))
[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

```