'''
Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz', 
then perform the following separate slice operations to obtain:
a) The first half of the string using starting and ending indices.
b) The first half of the string using only the ending index.
c) The second half of the string using starting and ending indices.
d) The second half of the string using only the starting index.
e) Every second letter in the string starting with 'a'.
f) The entire string in reverse.
'''

def main():
    alphabet = [chr(i) for i in range(97, 123)]
    print(f"\nOriginal:\n{alphabet}")
    print(alphabet[0:int(len(alphabet)/2)]) 
    print(alphabet[:int(len(alphabet)/2)])
    print(alphabet[int(len(alphabet)/2):len(alphabet)])
    print(alphabet[int(len(alphabet)/2):])
    print(alphabet[::2])
    print(alphabet[::-1])

main()
