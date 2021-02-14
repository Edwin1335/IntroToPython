'''
In each of the following expressions, replace the ***s
with a set operator that produces the result shown in the comment. The last operation
should check whether the left operand is an improper subset of the right operand. For each
of the first four expressions, specify the name of the set operation that produces the specified result.
a) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} # {1,2,4,8,16,64,256}
b) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} # {1,4,16}
c) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} # {2,8}
d) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} # {2,8,64,256}
e) {1, 2, 4, 8, 16} *** {1, 4, 16, 64, 256} # False
'''

def main():
    set1 = {1, 2, 4, 8, 16}
    set2 = {1, 4, 16, 64, 256}
    
    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.difference(set2))
    print(set1.symmetric_difference(set2))
    print(set1.issubset(set2))


main()
