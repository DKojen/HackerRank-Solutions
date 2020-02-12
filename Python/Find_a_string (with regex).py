#https://www.hackerrank.com/challenges/find-a-string/problem
#Find number of times that the substring occurs in the given string


import re
def count_substring(string, sub_string):
    count_substring = re.findall('(?='+sub_string+')',string)
    return len(count_substring)

    return len(re.findall('(?='+sub_string+')', string))
if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    
    count = count_substring(string, sub_string)
    print(count)
