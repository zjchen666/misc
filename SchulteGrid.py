import pandas as pd
from random import randint
import os

ROW = 5
COL = 5
size = ROW * COL
table_number = 5

def shuffle():
    nums = [i for i in range(size)]
    res  = [[i for i in xrange(COL)] for j in range(ROW)]

    for i in xrange(size):
        pos = randint(0, i)
        nums[i], nums[pos] = nums[pos], nums[i]
    
    for i in xrange(size):
        res[i / COL][i % COL] = nums[i]

    return res

def create_table():
    nums = shuffle()
    
    d = {}

    for i in range(ROW):
        d[i] = nums[i]

    df = pd.DataFrame(d)
    h = df.to_html(index=False, header=False)
    return h;
    
def create_file():
    os.remove("table.html")
    file = open("table.html",'a')

    for i in range(table_number):
        table = create_table()
        file.write(table)
        file.write("<br>")
        
    file.close()

create_file();
