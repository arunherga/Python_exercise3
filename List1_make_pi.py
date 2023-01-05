"""
21) List-1 > make_pi

Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


make_pi() → [3, 1, 4]

"""

def make_pi():
    pi = int(22/7 *100)
    return [int(x) for x in str(pi)]

if __name__ == '__main__':
    print(make_pi()) 
