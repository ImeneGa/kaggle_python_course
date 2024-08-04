def isInt(n):
    '''
    This function verifies either n is an integer or not
    '''
    try:
        int(n)
        return True
    except ValueError:
        return False

def to_smash(a, b, c):
    '''
    This function returns the number of candies every 3 kids will devide between themselves and those smashed, each one having a, b and c candies
    '''
    return [(a + b + c) // 3, ((a + b + c) // 3) % 3]

val = True
val2 = True
val3 = True
a = 0
b = 0
c = 0

while val:
    a = input('How much candies does Carol have?\n')
    if isInt(a):
        val = False
        while val2:
            b = input('How much candies does Tonny have?\n')
            if isInt(b):
                val2 = False
                while val3:
                    c = input('How much candies does Tor have?\n')
                    if isInt(c):
                        val3 = False
                        tab = to_smash(int(a), int(b), int(c))
                        print('Each one of Carol, Tony and Tor will have', tab[0], 'candies, and they will smach', tab[1], 'candies')
                    else:
                        print(c, 'is not an integer! Try again')
            else:
                print(b, 'is not an integer! Try again')
    else:
        print(a, 'is not an integer! Try again')
