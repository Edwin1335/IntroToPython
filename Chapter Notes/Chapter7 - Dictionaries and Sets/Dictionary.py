def sets():
    '''
    (IPython Session) Given the sets {10, 20, 30} and {5, 10, 15, 20}, use the mathematical set operators to produce the following sets:
    a) {30}
    b) {5, 15, 30}
    c) {5, 10, 15, 20, 30}
    d) {10, 20}
    '''
    set1 = {10, 20, 30}
    set2 = {5, 10, 15, 20}
    print(f"A: {set1 - set2}")
    print(f"B: {set1 ^ set2}")
    print(f"C: {set1 | set2}")
    print(f"C: {set(sorted(set1 | set2))}")
    print(f"D: {set2 & set1}")


sets()
