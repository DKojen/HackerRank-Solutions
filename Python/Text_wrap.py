#https://www.hackerrank.com/challenges/text-wrap/problem
#You are given a string  and width .
#Your task is to wrap the string into a paragraph of width .

import textwrap

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    result = wrap(string, max_width)
    print(result)

#or without using textwrap:
    
def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
