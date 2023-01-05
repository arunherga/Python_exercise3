"""
16) List-1 > middle_way

Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]


"""

def mid_way(a, b):
    return [a[int(len(a)//2)], b[int(len(b)//2)]]

if __name__ == '__main__':
    print(mid_way([1, 2, 3], [4, 5, 6]))
    print(mid_way([7, 7, 7], [3, 8, 0]))
    print(mid_way([5, 2, 9], [1, 4, 5]))