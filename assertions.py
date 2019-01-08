''' Learning testing in Python3 and TDD '''

# testing Assertions
def sumPosNumbers(a, b):
    assert a >= 0 and b >= 0, "Inputs need to be positive numbers"
    assert a != 0 and b != 0, "Inputs need to be non-zero numbers"
    return (a + b)


# print(sumPosNumbers(5, 3))
# print(sumPosNumbers(0, 6))
# print(sumPosNumbers(3, -5))

# testing w/ docstrings
def add(x, y):
    """
    >>> add(2, 3)
    5

    >>> add(100, 300)
    400

    """
    return x + y

def double(values):
    """
    >>> double([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None]):
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]

