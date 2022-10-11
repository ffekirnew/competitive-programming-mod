#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    sea_level = 0
    
    for step in range(steps):
        if path[step] == "D":
            sea_level -= 1
        elif path[step] == "U":
            sea_level += 1
        
        if sea_level == 0 and path[step] == "U":
            valleys += 1
    
    return valleys
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()