




'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators
'''


import regex as re


def splitkeep(s, delimiter):
    
    split = s.split(delimiter)

    for substr in split[:-1]:
        print(substr)

    print(split[-1])
                                 
    
    return [substr + delimiter for substr in split[:-1]] + [split[-1]]

def startpy():

    result = re.split('(\W)', 'foo/bar spam\neggs')
    # print(result)

    result = splitkeep('22 STODDARD ROAD PO BOX 165', 'PO BOX')
    print(result)

if __name__ == '__main__':
    startpy()