

# from sklearn.model_selection import train_test_split
from importlib import import_module
import sys

# Local
import constants as con
from constants import (STREET_NAME, HOUSE_NO, SUITE_NO, EMPTY)

PATTERNS_FOLDER = 'patterns/'

CSV_DELIM = ','

spaces_mapping = {
        1: 3,
        2: 2,
        3: 3,
        4: 4,
        5: 3,
        6: 2,
        7: 1,
        8: 4,
        9: 3,
        10: 2,
        11: 1
    }

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

def get_single_content(current_index, item, tag):

    content = ""

    content += f"{current_index}"
    content += f"{CSV_DELIM}{item}"
    content += f"{CSV_DELIM}{tag}"
    content += "\n"

    return content

def pattern_1_maker_single(current_index, address):

    '''
        12A WEST STREET
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):

        if(c_index == 0):
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            sub_parts = c_item.split(" ")

            for item in sub_parts:
                content += get_single_content(current_index, item, STREET_NAME)

    return content

def pattern_2_maker_single(current_index, address):

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
        content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_3_maker_single(current_index, address):

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

            content += get_single_content(current_index, sub_parts[0], SUITE_NO)
            content += get_single_content(current_index, sub_parts[1], HOUSE_NO)

        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_4_maker_single(current_index, address):

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

            content += get_single_content(current_index, sub_parts[0], SUITE_NO)
            content += get_single_content(current_index, "-", EMPTY)
            content += get_single_content(current_index, sub_parts[1], HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_5_maker_single(current_index, address):

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

            content += get_single_content(current_index, sub_parts[0], SUITE_NO)
            content += get_single_content(current_index, "/", EMPTY)
            content += get_single_content(current_index, sub_parts[1], HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_6_maker_single(current_index, address):

    '''
        Pattern 5:

        6	
        (StreetName) # (Suite_No)	
        marshfield dr # 495
        chanute chanute dr # 996
        willow willow causeway # 211

        Sample:
        marshfield dr # 495
    '''

    address_full_parts = address.split("#")

    address_parts = address_full_parts[0].split(" ")

    content = ""

    # print(address)
    # print(len(address_parts))

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)
        c_item = c_item.strip()
        if(len(c_item) > 0):
            content += get_single_content(current_index, c_item, STREET_NAME)
        
    content += get_single_content(current_index, "#", EMPTY)
    content += get_single_content(current_index, address_full_parts[1].strip(), SUITE_NO)

    return content


def pattern_7_maker_single(current_index, address):

    '''
        Pattern 7:
        
        7	
        (StreetName) (Suite_No) (StreetName)	        

        Sample:
        BOTANY TOWN CENTRE 588 CHAPEL ROAD

        Not clear
    '''

    raise Exception("Not Implemented")

def pattern_8_maker_single(current_index, address):

    '''
        Pattern :

        

        Sample:
        

        Not clear
    '''

    raise Exception("Not Implemented")

def pattern_9_maker_single(current_index, address):

    '''
        Pattern :

        

        Sample:
        
        Not clear
    '''

    raise Exception("Not Implemented")

def pattern_10_maker_single(current_index, address):

    '''
        Pattern 10:

        10	
        (House_No with Alphabet) (StreetName)	

        Sample:
        12A WEST STREET
    '''

    address_parts = address.split(" ")

    content = ""

    content += get_single_content(current_index, address_parts[0], HOUSE_NO)
    content += get_single_content(current_index, address_parts[1], STREET_NAME)
    content += get_single_content(current_index, address_parts[2], STREET_NAME)

    return content

def pattern_11_maker_single(current_index, address):

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

            content += get_single_content(current_index, sub_parts[0], SUITE_NO)
            content += get_single_content(current_index, "-", EMPTY)
            content += get_single_content(current_index, sub_parts[1], HOUSE_NO)

        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_12_maker_single(current_index, address):

    '''
        Pattern :

        12	
        (Suite_No) (House_No) (StreetName)	
        3820 43 AVE

        Sample:
        3820 43 AVE
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(current_index, c_item, SUITE_NO)

        elif(c_index == 1):

            content += get_single_content(current_index, c_item, HOUSE_NO)

        else:
            content += get_single_content(current_index, c_item, STREET_NAME)


    # print(content)

    return content

def pattern_13_maker_single(current_index, address):

    '''
        Pattern 13:

        1	
        (House_No) (StreetName) (UNIT) (Suite_No)
        
        Sample:
        23 CHEVIN Road UNIT 90
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(current_index, c_item, HOUSE_NO)

        elif(len(address_parts)-1 == c_index):

            content += get_single_content(current_index, c_item, SUITE_NO)

        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

#  
def pattern_14_maker_single(current_index, address):

    '''
        Pattern 14:

        14	
        (House_No) (HWY with No)	
        	
        Sample:
        575 HWY 21
    '''

    address_parts = address.split(" ")

    content = ""

    content += get_single_content(current_index, address_parts[0], HOUSE_NO)
    content += get_single_content(current_index, address_parts[1], STREET_NAME)
    content += get_single_content(current_index, address_parts[2], STREET_NAME)

    return content


def pattern_15_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)

        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_16_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_17_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    content += get_single_content(current_index, "PO BOX", HOUSE_NO)

    sub_address = main_address_parts[1].strip()
    content += get_single_content(current_index, sub_address, HOUSE_NO)

    return content

def pattern_18_maker_single(current_index, address):

    '''
        Pattern 17:

        18		

        Sample:
        103 PTH 12 N

        
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_19_maker_single(current_index, address):

    '''
        Pattern 19:

        19	
        (House_No) (HWY with No)	
        10 HWY

        Sample:
        

        
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_20_maker_single(current_index, address):

    '''
        Pattern 20:

        

        
    '''

    

    # print(content)

    raise Exception("Not Implemented")

def pattern_21_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)
            break
        
        content += get_single_content(current_index, c_item, SUITE_NO)

    # print(content)

    for c_index, c_item in enumerate(ad_list):

        if(c_index > int_index):
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_22_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)

            break
        
        content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_23_maker_single(current_index, address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''
    
    ad_list = address.split(" ")
    content = "" 

    for c_index, c_item in enumerate(ad_list):

        if(c_index == 0):
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content


def pattern_24_maker_single(current_index, address):

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

        content += get_single_content(current_index, c_item, HOUSE_NO)

        # if(c_index == 0):
        #     content += get_single_content(c_item, HOUSE_NO)
        # elif(c_index == 0):
        #     content += get_single_content(c_item, HOUSE_NO)
        # else:
        #     content += get_single_content(c_item, HOUSE_NO)

    return content

def pattern_25_maker_single(current_index, address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''

    

    # print(content)

    pass


def pattern_26_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, SUITE_NO)
        else:
            if(c_index == 2 and is_int(c_item)):
                content += get_single_content(current_index, c_item, HOUSE_NO)
                after_suite_flag = True
            else:
                content += get_single_content(current_index, c_item, STREET_NAME)
    # print(content)

    return content

def pattern_27_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:

            if(c_item == "STE" or c_item == "SUITE"):
                content += get_single_content(current_index, c_item, SUITE_NO)

                after_suite_flag = True
            else:

                if(after_suite_flag):
                    content += get_single_content(current_index, c_item, SUITE_NO)
                else:
                    content += get_single_content(current_index, c_item, STREET_NAME)

    # print(content)

    return content

def pattern_28_maker_single(current_index, address):

    '''
        Pattern 28:

        

        Sample:
        

        
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(current_index, c_item, HOUSE_NO)
        elif(len(address_parts)-1 == c_index):
            content += get_single_content(current_index, c_item, SUITE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_29_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_30_maker_single(current_index, address):

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
            content += get_single_content(current_index, c_item, HOUSE_NO)
        else:
            content += get_single_content(current_index, c_item, STREET_NAME)

    return content

def pattern_31_maker_single(current_index, address):

    pass

def pattern_32_maker_single(current_index, address):

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
    
    content += get_single_content(current_index, address_parts[0], STREET_NAME)
    content += get_single_content(current_index, address_parts[1], HOUSE_NO)

    return content

def pattern_maker_single(current_index, c_line, pattern_index):

    dynamic_module  = import_module(f"bert_pattern_maker")
    dynamic_method  = getattr(dynamic_module, f"pattern_{pattern_index}_maker_single")

    return dynamic_method(current_index, c_line)

def pattern_maker_multiple(pattern_index):

    file = f'{PATTERNS_FOLDER}pattern{pattern_index}.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    # train_list, test_list = train_test_split(lcurrent_indexines, train_size=0.8)

    global current_index

    if(con.PATTERN_DEBUG):
        print('Using Debug mode\n')
        lines = [lines[0]]

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        c_line = c_line.lower()

        current_index += 1

        content += pattern_maker_single(current_index, c_line, pattern_index)

    return content

def get_current_index():

    with open(con.ADDRESS_INPUT_BERT_CSV_PATH, 'r') as f:
        lines       = f.read().splitlines()
        last_line   = lines[-1]

        try:
            cu_index = int(last_line.split(CSV_DELIM)[0])
        except:
            return -1

        return cu_index
    
current_index = get_current_index()

def startpy():

    pattern = int(sys.argv[1])

    print(pattern_maker_multiple(pattern))    

if __name__ == '__main__':
    startpy()

'''
How to run?

python bert_pattern_maker.py <pattern_index>
python bert_pattern_maker.py 5
'''