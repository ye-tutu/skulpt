__author__ = 'bmiller'

def testEqual(actual, expected):
    if (
        type(expected) == type(1)
        and actual == expected
        or type(expected) != type(1)
        and type(expected) == type(1.11)
        and abs(actual - expected) < 0.00001
        or type(expected) != type(1)
        and type(expected) != type(1.11)
        and actual == expected
    ):
        print('Pass')
        return True
    print(f'Test Failed: expected {str(expected)} but got {str(actual)}')
    return False

def testNotEqual(actual, expected):
    pass

