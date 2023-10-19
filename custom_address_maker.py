




'''
Created on 

@author: Raja CSP Raman

source:
    
'''
import random

address_part_2023101801_str = """
dover, beacon, sylvester, winn, winnmere, sunnyside
"""

address_part_10002_str = """
3200 e sky harbor blvd
"""

def get_random_part(content):

    contents = content.lower().strip().split(',')

    return str(random.choice(contents)).strip()

'''
    Pattern 2023101801: (Oct 18, 2023 - 01)
    Number String1 String2
    10 DOVER DRIVE
'''
def pattern_2023101801():

    part1 = random.randint(1, 100)

    part2 = get_random_part(address_part_2023101801_str)
    part3 = get_random_part(address_part_10002_str)

    return f"{part1} {part2} {part3}"

def get_multiple_addresses():
    
    for _ in range(50):
        print(pattern_2023101801())

def startpy():
    
    get_multiple_addresses()

if __name__ == '__main__':
    startpy()