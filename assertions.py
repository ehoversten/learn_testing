''' Learning testing in Python3 and TDD '''

# Starting with Assertions
def sumPosNumbers(a, b):
    assert a >= 0 and b >= 0, "Inputs need to be positive numbers"
    assert a != 0 and b != 0, "Inputs need to be non-zero numbers"
    return (a + b)


print(sumPosNumbers(5, 3))
print(sumPosNumbers(0, 6))
print(sumPosNumbers(3, -5))

