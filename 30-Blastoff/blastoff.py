# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    for i in range(n, 0, -1):
        print i
    print 'Blastoff!'




countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


