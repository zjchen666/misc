import os
from random import randint
import sys
print sys.argv


COLUMNS = 4
ROWS = 15

filename = "math.txt"
path = os.getcwd()
print path
fd = open(filename, 'w')
fd.write("$ Julia Is Math Fairy $                  Your Score Is: ___________ \n\n\n")
fd.write('\n')

rows = ROWS

while rows:
    columns = COLUMNS
    while columns:
        num1 = randint(1, 9)
        num2 = randint(5, 9)
        equation = str(num1) + ' ' + '+' + ' ' + str(num2) + ' ' + ' ' + '=' + '     '
        print equation
        fd.write( equation + '\t')
        #fd.write('\t')
        columns -= 1
    fd.write('\n\n\n')
    rows -= 1

fd.close()

