"""
    1) String-1 > hello_name
    
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


    hello_name('Bob') → 'Hello Bob!'
    hello_name('Alice') → 'Hello Alice!'
    hello_name('X') → 'Hello X!'

"""

def hello_name(name):
    return ("Hello %s"%(name))

if __name__ == '__main__':
    print(hello_name("Bob"))
    print(hello_name("Alice"))
    print(hello_name("X"))