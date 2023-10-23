




'''
Created on 

@author: Raja CSP Raman

source:
    
'''
import random
import sys
from importlib import import_module

MAX_ADDRESS_COUNT = 50

dynamic_module  = import_module(f"custom_address_maker")

address_part_2023101801_str = """
dover, beacon, sylvester, winn, winnmere, sunnyside
"""

address_part_10002_str = """
3200 e sky harbor blvd
"""

address_part_13_20231023_1 = """
chanute, travis, main, elm, maple, oak, birch, cedar, spruce, pine, redwood, spruce, willow, marshfield, terrace, wyresdale, 
neville, laity, temple, shaftesbury, hills, patrick, bentrim
"""

address_part_13_20231023_2 = """
rd, road, st, street, ave, avenue, lane, crt, court, drive, dr, causeway,
"""

address_part_13_20231023_3 = """
unit, unt, unit, unit
"""

def get_random_part(content):

    contents = content.lower().strip()

    content = ','.join(word for word in content.split(',') if len(word)>0)
    content_list = content.split(',')

    new_content_list = []

    for item in content_list:
        item = item.strip().replace('\n', '')
        
        if(len(item) < 1):
            continue
        new_content_list.append(item)

    return str(random.choice(new_content_list)).strip()

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

    return f"{part1} {part2} {part3} {part4} {part5}"

def pattern_2_maker_single():

    '''
        marshfield bank
    '''

    part1 = grp(address_part_13_20231023_1)
    part2 = grp(address_part_13_20231023_2)

    return f"{part1} {part2}"

def get_multiple_addresses(pattern_index):

    
    dynamic_method  = getattr(dynamic_module, f"pattern_{pattern_index}_maker_single")
    
    for _ in range(MAX_ADDRESS_COUNT):
        print(dynamic_method())

def startpy():

    pattern = int(sys.argv[1])
    
    # get_multiple_addresses(pattern)

    for _ in range(100):

        print(grp(address_part_13_20231023_2))

if __name__ == '__main__':
    startpy()