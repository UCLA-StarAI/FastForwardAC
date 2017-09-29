#
# Python file to receive a forward feed .ac file and create a c file 
# to calculate marginal probabilities
# 
# By: Andrew Jemin Choi 
#

import sys
import math
import datetime

num = 0 # line number in original file
size = 100000

# Check if file was passed by command line
FILE_NAME = ''
if (len(sys.argv) < 2):
    FILE_NAME = input("Please input an AC file: ")
else:    
    FILE_NAME = sys.argv[1]
    #size = sys.argv[2]

out_code = ''
    
out_code += "\tdouble vr[" + str(size) + "];\n"
    
# Read the AC file
AC_FILE = open(FILE_NAME, 'r') 
for line in AC_FILE:
    #print(line)
    if line[0] == '(':
        print("\t ... reading file ...")
    elif line[0] == 'E':
        print("\t ... done reading file ...")
        break
    else:
        parsed = line.split()

        if parsed[0] == 'n':
            out_code += "\tvr[" + str(num) + "] = " + str(parsed[1]) + ";\n"
        elif parsed[0] == 'v':
            out_code += "\tvr[" + str(num) + "] = " + str(parsed[2]) + ";\n"
        elif parsed[0] == '+':
            out_code += "\tvr[" + str(num) + "] = "
            isFirst = True
            for child in parsed:
                if child == '+':
                    #nothing
                    pass
                elif isFirst:
                    out_code += "vr[" + child + "]"
                    isFirst = False
                else:
                    out_code += " + vr[" + child + "]"

            out_code += ";\n"

        elif parsed[0] == '*':
            out_code += "\tvr[" + str(num) + "] = "
            isFirst = True
            for child in parsed:
                if child == '*':
                    #nothing
                    pass
                elif isFirst:
                    out_code += "vr[" + child + "]"
                    isFirst = False
                else:
                    out_code += " * vr[" + child + "]"

            out_code += ";\n"

        num += 1

# Print the output
num -= 1
out_code += '\tprintf("output: (%lf)", log10(vr[' + str(num) + ']));'

# Write to a test file
f = open('test.c', 'w')
currentDate = ((str)(datetime.datetime.now().month) + '-'
               + (str)(datetime.datetime.now().day) + '-'
               + (str)(datetime.datetime.now().year))
header = '''/*
* Cache-propagation using Arithmetic Circuits
*
* Author: Andrew Choi
*
* File created on: ''' + currentDate + '''\n*/'''

code = '''
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(int argc, char** argv) {
'''

code += out_code

code += '''
}
'''

print(code)

f = open('forward_test.c', 'w')
f.write(code)
f.close
