class OutofRangeError(Exception):
    pass


def numberName(a):
    if a == 1:
        return print('one')
    elif a == 2:
        return print('two')
    elif a == 3:
        return print('three')
    else:
        raise OutofRangeError


try:
    numberName(4)
except OutofRangeError:
    print("That's not one of the allowed values!")
