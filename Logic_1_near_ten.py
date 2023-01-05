"""
33)Logic-1 > near_ten

    Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
    Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


    near_ten(12) → True
    near_ten(17) → False
    near_ten(19) → True

"""
def near_ten(num):
    reminder = num % 10
    rem = [1,2,8,9]

    if reminder in rem:
        return True
    else: return False

if __name__ == '__main__':
    print(near_ten(12))
    print(near_ten(17))
    print(near_ten(19))