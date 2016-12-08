# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.





#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9

def biggest(a, b, c):
    largest_number = max(a, b, c)
    return largest_number
