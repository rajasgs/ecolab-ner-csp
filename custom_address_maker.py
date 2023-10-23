




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

address_part_13_20231023_1 = """
chanute, travis, main, elm, maple, oak, birch, cedar, spruce, pine, redwood, spruce, willow
"""

address_part_13_20231023_2 = """
rd, road, st, street, ave, avenue, lane, crt, court, drive, dr
"""

address_part_13_20231023_3 = """
unit, unt, unit, unit
"""

def get_random_part(content):

    contents = content.lower().strip().split(',')

    return str(random.choice(contents)).strip()

def get_house_no():

    return random.randint(1, 1000)

grp = get_random_part

'''
    Pattern 2023101801: (Oct 18, 2023 - 01)
    Number String1 String2
    10 DOVER DRIVE
'''
def pattern_2023101801():

    part1 = get_house_no()

    part2 = get_random_part(address_part_2023101801_str)
    part3 = get_random_part(address_part_10002_str)

    return f"{part1} {part2} {part3}"

def pattern_13_20231023():

    part1 = get_house_no()

    part2 = grp(address_part_13_20231023_1)
    part3 = grp(address_part_13_20231023_2)
    part4 = grp(address_part_13_20231023_3)
    part5 = get_house_no()

    address_part_13_20231023_3

    return f"{part1} {part2} {part3} {part4} {part5}"

def get_multiple_addresses():
    
    for _ in range(50):
        # print(pattern_2023101801())

        print(pattern_13_20231023())

        pass

def startpy():
    
    get_multiple_addresses()

if __name__ == '__main__':
    startpy()