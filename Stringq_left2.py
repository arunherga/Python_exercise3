"""
8) String-1 > left2

    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


    left2('Hello') → 'lloHe'
    left2('java') → 'vaja'
    left2('Hi') → 'Hi'


"""

def left2(str):
    return str[2:len(str)]+str[0:2]


if __name__ == '__main__':
    print(left2('Hello'))
    print(left2('java'))
    print(left2('Hi'))