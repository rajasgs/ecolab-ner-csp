




'''
Created on 

@author: Raja CSP Raman

source:
    
'''
import random
import sys
from importlib import import_module
import string

MAX_ADDRESS_COUNT = 100

dynamic_module  = import_module(f"custom_address_maker")

address_part_2023101801_str = """
dover, beacon, sylvester, winn, winnmere, sunnyside
"""

address_part_10002_str = """
3200 e sky harbor blvd
"""

address_part_13_20231023_1 = """
chanute, travis, main, elm, maple, oak, birch, cedar, spruce, pine, redwood, spruce, willow, marshfield, terrace, wyresdale, 
neville, laity, temple, shaftesbury, hills, patrick, bentrim, westgate, park, 
"""

address_part_13_20231023_2 = """
rd, road, st, street, ave, avenue, lane, crt, court, drive, dr, causeway,
"""

address_part_13_20231023_3 = """
unit, unt, unit, unit
"""



def get_random_part(content):

    content = content.lower().strip()

    content = ','.join(word for word in content.split(',') if len(word)>0)
    content_list = content.split(',')

    new_content_list = []

    for item in content_list:
        item = item.strip().replace('\n', '')
        
        if(len(item) < 1):
            continue
        new_content_list.append(item)

    return str(random.choice(new_content_list)).strip()

def get_random_no():

    return random.randint(1, 1000)

def get_random_character():

    return str(random.choice(string.ascii_letters)).lower()

def get_house_no():

    return get_random_no()

def get_random_boolean():

    rno = get_random_no()

    if(rno % 2 == 0):
        return True
    
    return False

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

def pattern_5_maker_single():

    '''
        1/3 westgate park fodderwick
    '''

    part1 = grp(address_part_13_20231023_1)
    part2 = grp(address_part_13_20231023_1)

    final_part = f"{get_random_no()}/{get_random_no()} {part1} {part2}"

    if(get_random_boolean()):
        final_part = f"{final_part} {grp(address_part_13_20231023_2)}"

    return final_part

def pattern_6_maker_single():

    '''
        calle nueva york # 301
        5535 irwin simpson rd # 5535
        808 cosby hwy # 1540
    '''

    part1 = grp(address_part_13_20231023_1)
    part2 = grp(address_part_13_20231023_2)

    final_part = f""

    if(get_random_boolean()):
        final_part += f"{part1} "
    
    final_part += f"{part1} {part2} # {get_random_no()}"

    return final_part

def pattern_10_maker_single():

    '''
        172a robinhood ave
    '''

    part1 = f"{get_random_no()}{get_random_character()}"

    part2 = grp(address_part_13_20231023_1)
    part3 = grp(address_part_13_20231023_2)

    final_part = f""
    
    final_part += f"{part1} {part2} {part3}"

    return final_part

def get_multiple_addresses(pattern_index):

    dynamic_method  = getattr(dynamic_module, f"pattern_{pattern_index}_maker_single")
    
    for _ in range(MAX_ADDRESS_COUNT):
        print(dynamic_method())

def startpy():

    pattern = int(sys.argv[1])
    
    get_multiple_addresses(pattern)

if __name__ == '__main__':
    startpy()