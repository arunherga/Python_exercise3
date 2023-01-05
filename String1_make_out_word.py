"""
2)String-1 > make_out_word

    Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


    make_out_word('<<>>', 'Yay') → '<<Yay>>'
    make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
    make_out_word('[[]]', 'word') → '[[word]]'

"""

def make_out_word(out, word):
    symbol_1 = out[0:len(out)//2]
    symbol_2 = out[len(out)//2:]
    return (symbol_1+word+symbol_2)

if __name__ == '__main__':
    print(make_out_word('<<>>', 'Yay'))
    print(make_out_word('<<>>', 'WooHoo'))
    print(make_out_word('[[]]', 'word'))