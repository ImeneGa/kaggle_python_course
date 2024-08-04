def fashionably_late(arrivals, name):
    """This function returns if someone is fashionably late from a list of guests except if she/he is the last one
    """
    a = arrivals.index(name)
    return (a >= len(arrivals) / 2) and (a != len(arrivals) - 1)

val = True

sentence = input('Write the name of the guests attending your party, all in one line with space between each one of them\n')
tab = sentence.split(' ')
while val:
    guest = input('Write the name of the guest you want to check if she/he is fashionably late\n')
    if not (guest in tab):
        print(guest, 'is not a guest! Try again')
    else:
        val = False
        val2 = fashionably_late(tab, guest)
        print(guest, 'is' if val2 else 'is not', 'fashionably late')