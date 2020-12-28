'''
Reimplement your script using a for loop and the f-string capabilities you
learned in this chapter to produce the following table with the numbers right aligned in
each column.
number square cube
 0 0 0
 1 1 1
 2 4 8
 3 9 27
 4 16 64
 5 25 125
'''
#Loop 10 times
for x in range(1, 11):
    if x == 1:
        print("Numbers Squares Cube")
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
