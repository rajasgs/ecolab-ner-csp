
'''

Created on 

@author: Raja CSP Raman

source:
    
    Address-CNER-Riversand
    https://docs.google.com/spreadsheets/d/1QH_T6C3MAJNj5f_1gL1dZtLRUjFbwJ4wcHpPwlCfylI/edit#gid=968221325

    https://www.kaggle.com/rajacsp/address-pattern/

    https://stackoverflow.com/questions/31627321/testing-if-a-value-is-numeric

    
'''

# import numbers
from sklearn.model_selection import train_test_split
from importlib import import_module
import sys

# Local
import constants as con
from constants import (STREET_NAME, HOUSE_NO, SUITE_NO, EMPTY)

PATTERNS_FOLDER = 'patterns/'

def get_spaces(content):

    if(len(content) < 3):
        return (" " * (4 - len(content)))
    
    if(len(content) < 8):
        return (" " * (8 - len(content)))
    
    if(len(content) < 12):
        return (" " * (12 - len(content)))
    
    if(len(content) < 16):
        return (" " * (16 - len(content)))
    
    if(len(content) < 20):
        return (" " * (20 - len(content)))
    
    if(len(content) < 24):
        return (" " * (24 - len(content)))
    
    if(len(content) < 28):
        return (" " * (28 - len(content)))

    return ""

def convert_num(s):
    try:
        return int(s)
    except ValueError:
        return s
    
def is_int(c_item):

    c_item = convert_num(c_item.strip())

    return (isinstance(c_item, int))


def find_digit_index_in_list(address_list):

    for c_index, c_item in enumerate(address_list):

        # print(f'{c_index} : [{c_item}] : {isinstance(c_item, numbers.Number)}')

        if(is_int(c_item)):
            return c_index

    return 0

def get_single_content(item, tag):

    content = ""

    content += f"{item}"
    content += f"{get_spaces(item)}"
    content += f"{tag}"
    content += "\n"

    return content

def pattern_1_maker_single(address):

    '''
        Pattern 1:

        1	
        (House_No) (StreetName)	
        
        Sample:
        14 KINGSFORD SMITH AVE
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            sub_parts = c_item.split(" ")

            for item in sub_parts:
                content += get_single_content(item, STREET_NAME)

    return content


def pattern_2_maker_single(address):

    '''
        Pattern 2:

        2
        (Street_Name)		
        
        Sample:
        NEVILLE STREET
    '''

    address_parts = address.split(" ")

    content = ""

    for c_item in address_parts:
        content += get_single_content(c_item, STREET_NAME)

    return content


def pattern_3_maker_single(address):

    '''
        Pattern 3:

        3	
        (Suite_No)-(House_No) (StreetName)

        Sample:
        1626-1630 NESS AVE
    '''

    address_parts = address.split(" ")

    content = ""

    

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            sub_parts = c_item.split("-")

            content += get_single_content(sub_parts[0], SUITE_NO)
            content += get_single_content(sub_parts[1], HOUSE_NO)

        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_4_maker_single(address):

    '''
        Pattern 4:

        4	
        (Suite_No)-(House_No) (StreetName_with_Number)	
        1701-1799 HIGHWAY 2 W

        Sample:
        1701-1799 HIGHWAY 2 W
    '''

    address_parts = address.split(" ")

    # print(len(address_parts))

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):

            sub_parts = c_item.split("-")

            content += get_single_content(sub_parts[0], SUITE_NO)
            content += get_single_content("-", EMPTY)
            content += get_single_content(sub_parts[1], HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_5_maker_single(address):

    '''
        Pattern 5:

        5	
        (Suite_No)/(House_No) (StreetName)	
        55/57 BAHNHOFSTRASSE

        Sample:
        1/3 WESTGATE PARK FODDERWICK
    '''

    # print(address)

    address_parts = address.split(" ")

    # print(len(address_parts))

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):

            sub_parts = c_item.split("/")

            content += get_single_content(sub_parts[0], SUITE_NO)
            content += get_single_content("/", EMPTY)
            content += get_single_content(sub_parts[1], HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_6_maker_single(address):

    '''
        Pattern 6:

        6	
        (StreetName) # (Suite_No)	
        CALLE NUEVA YORK # 301

        Sample:
        5535 IRWIN SIMPSON RD # 5535
    '''

    # print(address)
    # print(len(address_parts))

    address_full_parts = address.split("#")

    address_parts = address_full_parts[0].split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        c_item = c_item.strip()
        if(len(c_item) <= 0):
            continue

        if(c_index == 0):
            
            if(isinstance(c_item, int)):
                content += get_single_content(c_item, HOUSE_NO)
            else:
                content += get_single_content(c_item, STREET_NAME)

        else:
            content += get_single_content(c_item, STREET_NAME)
        
    
    content += get_single_content("#", EMPTY)
    content += get_single_content(address_full_parts[1].strip(), SUITE_NO)

    return content


def pattern_7_maker_single(address):

    '''
        Pattern 7:        
        7	
        
        801 route 38

    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_8_maker_single(address):

    '''
        Pattern 18:

        18		

        Sample:
        5535 irwin simpson rd # 5535

        
    '''

    address_full_parts = address.split("#")

    address_parts = address_full_parts[0].split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        c_item = c_item.strip()
        if(len(c_item) <= 0):
            continue

        if(c_index == 0):
            
            if(isinstance(c_item, int)):
                content += get_single_content(c_item, HOUSE_NO)
            else:
                content += get_single_content(c_item, STREET_NAME)

        else:
            content += get_single_content(c_item, STREET_NAME)
        
    content += get_single_content("#", EMPTY)
    content += get_single_content(address_full_parts[1].strip(), SUITE_NO)

    return content

def pattern_9_maker_single(address):

    '''
        Pattern :

        Sample:
        28 15th avenue s
    '''

    address_parts = address.split(" ")

    # print(len(address_parts))

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_10_maker_single(address):

    '''
        Pattern 10:

        10	
        (House_No with Alphabet) (StreetName)	

        Sample:
        12A WEST STREET
    '''

    address_parts = address.split(" ")

    content = ""

    content += get_single_content(address_parts[0], HOUSE_NO)
    content += get_single_content(address_parts[1], STREET_NAME)
    content += get_single_content(address_parts[2], STREET_NAME)

    return content

def pattern_11_maker_single(address):

    '''
        Pattern :

        (House_No with Alphabet)-(House_No with Alphabet) (StreetName)	

        Sample:
        200A-200B LAKESHORE DR

        Redundant
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):

        if(c_index == 0):
                
            sub_parts = address_parts[0].split("-")

            content += get_single_content(sub_parts[0], SUITE_NO)
            content += get_single_content("-", EMPTY)
            content += get_single_content(sub_parts[1], HOUSE_NO)

        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_12_maker_single(address):

    '''
        Pattern 12:
        12
        51 pinewood haven apt 50

        Sample:
        
    '''

    address_parts = address.split(" ")

    content = ""

    words_count = len(address_parts)

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        elif((c_index == ((words_count)-2)) or (c_index == ((words_count)-1))): # last item or last second item
            content += get_single_content(c_item, SUITE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_13_maker_single(address):

    '''
        Pattern 13:

        1	
        (House_No) (StreetName) (UNIT) (Suite_No)
        
        Sample:
        23 CHEVIN Road UNIT 90
    '''

    address_parts = address.split(" ")

    content = ""

    words_count = len(address_parts)

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        elif((c_index == ((words_count)-2)) or (c_index == ((words_count)-1))): # last item or last second item
            content += get_single_content(c_item, SUITE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

#  
def pattern_14_maker_single(address):

    '''
        Pattern 14:

        14	
        (House_No) (HWY with No)	
        	
        Sample:
        575 HWY 21
    '''

    address_parts = address.split(" ")

    content = ""

    content += get_single_content(address_parts[0], HOUSE_NO)
    content += get_single_content(address_parts[1], STREET_NAME)
    content += get_single_content(address_parts[2], STREET_NAME)

    return content


def pattern_15_maker_single(address):

    '''
        Pattern 15:

        15	
        (Street_No) (street_with_highway_in_hash_and_number)	
        409 HIGHWAY #4 N	

        Sample:
        409 HIGHWAY #4 N
 
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)

        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_16_maker_single(address):

    '''
        Pattern 16:

        16	
        (Street_Name) ( Street_No)	
        JURIJA GAGARINA 16

        Sample:
        JURIJA GAGARINA 16

        
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == len(address_parts) - 1):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content


def pattern_17_maker_single(address):

    '''
        Pattern 17:

        17	
        ( Street_No) (Street_Name) (Post_Box_No)	
        

        Sample:
        99 LEVEN STREET PO BOX 7159

        
    '''

    main_address_parts = address.split("po box")

    address_parts = main_address_parts[0].split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        c_item = c_item.strip()

        if(len(c_item) == 0):
            continue

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    content += get_single_content("po", SUITE_NO)
    content += get_single_content("box", SUITE_NO)

    sub_address = main_address_parts[1].strip()
    content += get_single_content(sub_address, SUITE_NO)

    return content







def pattern_20_maker_single(address):

    '''
        Pattern 20:

        

        
    '''

    

    # print(content)

    pass



def pattern_21_maker_single(address):

    '''
        Pattern 17:

        21	
        (House_name) (House_No) (Street_Name)	
        

        Sample:
        TOWN HALL HOUSE 456 KENT ST

    '''

    ad_list = address.split(" ")
    int_index = find_digit_index_in_list(ad_list)

    # print(int_index)

    content = ""

    for c_index, c_item in enumerate(ad_list):

        if(c_index == int_index):
            content += get_single_content(c_item, HOUSE_NO)
            break
        
        content += get_single_content(c_item, SUITE_NO)

    # print(content)

    for c_index, c_item in enumerate(ad_list):

        if(c_index > int_index):
            content += get_single_content(c_item, STREET_NAME)

    return content


def pattern_22_maker_single(address):

    '''
        Pattern 22:

        22	
        (Street_Name) ( Suite_No)	
        RUA PROFESSOR SIMÃO HESS, 341

        Sample:
        
    '''
    ad_list = address.split(" ")
    content = "" 

    for c_index, c_item in enumerate(ad_list):

        if(c_index == (len(ad_list)-1)):
            content += get_single_content(c_item, HOUSE_NO)

            break
        
        content += get_single_content(c_item, STREET_NAME)

    return content


def pattern_23_maker_single(address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''
    
    ad_list = address.split(" ")
    content = "" 

    for c_index, c_item in enumerate(ad_list):

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content


def pattern_24_maker_single(address):

    '''
        Pattern 24:

        24	
        (Post_Box) (Post_Box_No)	

        Sample:
        PO BOX 2247
    
    '''

    ad_list = address.split(" ")
    content = "" 

    for c_index, c_item in enumerate(ad_list):

        content += get_single_content(c_item, HOUSE_NO)

        # if(c_index == 0):
        #     content += get_single_content(c_item, HOUSE_NO)
        # elif(c_index == 0):
        #     content += get_single_content(c_item, HOUSE_NO)
        # else:
        #     content += get_single_content(c_item, HOUSE_NO)

    return content

def pattern_25_maker_single(address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''

    

    # print(content)

    pass


def pattern_26_maker_single(address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''

    address_parts = address.split(" ")
    content = "" 
    unit_finished_flag = False

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        c_item = c_item.strip()

        if(c_index == 0 or c_index == 1):
            content += get_single_content(c_item, SUITE_NO)
        else:
            if(c_index == 2 and is_int(c_item)):
                content += get_single_content(c_item, HOUSE_NO)
                after_suite_flag = True
            else:
                content += get_single_content(c_item, STREET_NAME)
    # print(content)

    return content
    

def pattern_27_maker_single(address):

    '''
        Pattern 17:

        27	
        ( Street_No) (Street_Name) (Postal_no)	
        

        Sample:
        2643 COMMERCIAL CENTER BLVD STE C300

    '''

    address_parts       = address.split(" ")
    content             = "" 
    after_suite_flag    = False

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        c_item = c_item.strip()

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:

            if(c_item == "STE" or c_item == "SUITE"):
                content += get_single_content(c_item, SUITE_NO)

                after_suite_flag = True
            else:

                if(after_suite_flag):
                    content += get_single_content(c_item, SUITE_NO)
                else:
                    content += get_single_content(c_item, STREET_NAME)

    # print(content)

    return content

def pattern_28_maker_single(address):

    '''
        Pattern 28:

        

        Sample:
        

        
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        elif(len(address_parts)-1 == c_index):
            content += get_single_content(c_item, SUITE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_29_maker_single(address):

    '''
        Pattern 29:

        29	
        (Street_No) (street_with_highway_in_number)	
        12128 S US HIGHWAY 71        

        Sample:
        12128 S US HIGHWAY 71
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_30_maker_single(address):

    '''
        Pattern 30:

        30	
        (Street_Name)(House_No)     

        Sample:
        Spadina Road 29
    '''

    address_parts = address.split(" ")

    content = ""

    count = len(address_parts)

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)
        if(c_index == (count - 1)):
            content += get_single_content(c_item, HOUSE_NO)
        else:
            content += get_single_content(c_item, STREET_NAME)

    return content

def pattern_31_maker_single(address):

    pass

def pattern_32_maker_single(address):

    '''
        Pattern 32:

        1	
        (Street_Name_Single_Word)(House_No)
        
        Sample:
        drottninggatan 7
    '''

    address_parts = address.split(" ")

    content = ""

    if(len(address_parts) > 2):
        return ""
    
    content += get_single_content(address_parts[0], STREET_NAME)
    content += get_single_content(address_parts[1], HOUSE_NO)

    return content

def pattern_43_maker_single(address):

    return pattern_15_maker_single(address)

def pattern_41_maker_single(address):

    return pattern_16_maker_single(address)

def pattern_maker_single(c_line, pattern_index):

    dynamic_module  = import_module(f"pattern_maker")
    dynamic_method  = getattr(dynamic_module, f"pattern_{pattern_index}_maker_single")

    return dynamic_method(c_line)

def pattern_maker_multiple(pattern_index):

    file = f'{PATTERNS_FOLDER}pattern{pattern_index}.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    train_list, test_list = train_test_split(lines, train_size=0.8)

    if(con.PATTERN_DEBUG):
        print('Using Debug mode\n')
        print(f'{train_list[0]}')
        print(f'{test_list[0]}')
        train_list = [train_list[0]]
        test_list = [test_list[0]]

    for c_line in train_list:
        c_line = c_line.replace('\n', '')

        c_line = c_line.lower()

        content += pattern_maker_single(c_line, pattern_index)

        content += "\n"

    content += str(f'-' * 50 + "\n")

    for c_line in test_list:
        c_line = c_line.replace('\n', '')

        c_line = c_line.lower()

        content += pattern_maker_single(c_line, pattern_index)

        content += "\n"

    # print(content)

    return content

def startpy():

    pattern = int(sys.argv[1])

    print(pattern_maker_multiple(pattern))


def test_split():

    main_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    train_list, test_list = train_test_split(main_list, train_size=0.8)

    print(train_list)
    print(test_list)

def test_2():

    pattern_index   = 1
    c_line          = "4591 N Pine Lane"

    # pattern_index   = 2
    # c_line          = "BENTRIM ROAD"

    dynamic_module  = import_module(f"pattern_maker")
    dynamic_method  = getattr(dynamic_module, f"pattern_{pattern_index}_maker_single")

    return dynamic_method(c_line)

    if(pattern_index == 1):
        return pattern_1_maker_single(c_line)
    elif(pattern_index == 2):
        return pattern_2_maker_single(c_line)

if __name__ == '__main__':
    
    
    startpy()

    # test_split()

    # print(test_2())

    pass


'''
How to run?

py pattern_maker.py <pattern_index>
py pattern_maker.py 13


This will print both training and testing content.
You need to copy paste both on appropriate text files



'''