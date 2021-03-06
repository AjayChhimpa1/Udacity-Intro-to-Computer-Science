# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string,n):
    new_string = ''
    for char in string:
        new = shift_n_letters(char, n)
        new_string = new_string + new
    return new_string


def shift_n_letters(letter, n):
    if letter == ' ':
        return ' '
    elif ord(letter) + n > ord('z'):
        return chr(ord(letter) + n + 96 - ord('z'))
    elif ord(letter) + n < ord('a'):
        return chr(ord(letter) + n + 26)
    else:
        return chr(ord(letter) + n)        


print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu', 13)
#>>> 'sarah'
print rotate('dave', 5)
#>>>'ifaj'
print rotate('ifaj', -5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"), -17)
#>>> ???
