"""
    3)String-1 > first_half

    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


    first_half('WooHoo') → 'Woo'
    first_half('HelloThere') → 'Hello'
    first_half('abcdef') → 'abc'

"""

def first_half(word):
    return word[:len(word)//2]

if __name__ == '__main__':
    print(first_half("WooHoo"))
    print(first_half("HelloThere"))
    print(first_half('abcfef'))