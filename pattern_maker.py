
'''

Created on 

@author: Raja CSP Raman

source:
    
    Address-CNER
    https://docs.google.com/spreadsheets/d/1QH_T6C3MAJNj5f_1gL1dZtLRUjFbwJ4wcHpPwlCfylI/edit#gid=968221325

    https://www.kaggle.com/rajacsp/address-pattern/
'''

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

    return ""

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

    content += f"{address_parts[0]}"
    content += f"{get_spaces(address_parts[0])}"
    content += "HOUSE_NO"
    content += "\n"

    content += f"{address_parts[1]}"
    content += f"{get_spaces(address_parts[1])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[2]}"
    content += f"{get_spaces(address_parts[2])}"
    content += "STREET_NAME"

    # print(content)

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

        content += f"{c_item}"
        content += f"{get_spaces(c_item)}"
        content += "STREET_NAME"
        content += "\n"

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

    sub_parts = address_parts[0].split("-")

    content += f"{sub_parts[0]}"
    content += f"{get_spaces(sub_parts[0])}"
    content += "SUITE_NO"
    content += "\n"

    content += f"{sub_parts[1]}"
    content += f"{get_spaces(sub_parts[1])}"
    content += "HOUSE_NO"
    content += "\n"

    content += f"{address_parts[1]}"
    content += f"{get_spaces(address_parts[1])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[2]}"
    content += f"{get_spaces(address_parts[2])}"
    content += "STREET_NAME"

    # print(content)

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

    content = ""

    sub_parts = address_parts[0].split("-")

    content += f"{sub_parts[0]}"
    content += f"{get_spaces(sub_parts[0])}"
    content += "SUITE_NO"
    content += "\n"

    content += f"-"
    content += f"{get_spaces('-')}"
    content += "0"
    content += "\n"

    content += f"{sub_parts[1]}"
    content += f"{get_spaces(sub_parts[1])}"
    content += "HOUSE_NO"
    content += "\n"

    content += f"{address_parts[1]}"
    content += f"{get_spaces(address_parts[1])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[2]}"
    content += f"{get_spaces(address_parts[2])}"
    content += "STREET_NAME"

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

            content += f"{sub_parts[0]}"
            content += f"{get_spaces(sub_parts[0])}"
            content += "SUITE_NO"
            content += "\n"

            content += f"-"
            content += f"{get_spaces('/')}"
            content += "0"
            content += "\n"

            content += f"{sub_parts[1]}"
            content += f"{get_spaces(sub_parts[1])}"
            content += "HOUSE_NO"
            content += "\n"
        else:
            content += f"{c_item}"
            content += f"{get_spaces(c_item)}"
            content += "STREET_NAME"
            content += "\n"

    return content

def pattern_6_maker_single(address):

    '''
        Pattern 5:

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

        if(c_index == 0):
            
            if(isinstance(c_item, int)):
                content += f"{c_item}"
                content += f"{get_spaces(c_item)}"
                content += "SUITE_NO"
                content += "\n"
            else:
                content += f"{c_item}"
                content += f"{get_spaces(c_item)}"
                content += "STREET_NAME"
                content += "\n"
        else:
            content += f"{c_item}"
            content += f"{get_spaces(c_item)}"
            content += "STREET_NAME"
            content += "\n"
        
    
    content += f"#"
    content += f"{get_spaces('#')}"
    content += "0"
    content += "\n"

    content += f"{address_full_parts[1]}"
    content += f"{get_spaces(address_full_parts[1])}"
    content += "0"
    content += "\n"

    return content


def pattern_7_maker_single(address):

    pass

def pattern_8_maker_single(address):

    pass

def pattern_9_maker_single(address):

    pass

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

    content += f"{address_parts[0]}"
    content += f"{get_spaces(address_parts[0])}"
    content += "HOUSE_NO"
    content += "\n"

    content += f"{address_parts[1]}"
    content += f"{get_spaces(address_parts[1])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[2]}"
    content += f"{get_spaces(address_parts[2])}"
    content += "STREET_NAME"

    # print(content)

    return content

def pattern_11_maker_single(address):

    pass

def pattern_12_maker_single(address):

    pass

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

    content += f"{address_parts[0]}"
    content += f"{get_spaces(address_parts[0])}"
    content += "HOUSE_NO"
    content += "\n"

    content += f"{address_parts[1]}"
    content += f"{get_spaces(address_parts[1])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[2]}"
    content += f"{get_spaces(address_parts[2])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[3]}"
    content += f"{get_spaces(address_parts[3])}"
    content += "SUITE_NO"
    content += "\n"

    content += f"{address_parts[4]}"
    content += f"{get_spaces(address_parts[4])}"
    content += "SUITE_NO"

    # print(content)

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

    content += f"{address_parts[0]}"
    content += f"{get_spaces(address_parts[0])}"
    content += "HOUSE_NO"
    content += "\n"

    content += f"{address_parts[1]}"
    content += f"{get_spaces(address_parts[1])}"
    content += "STREET_NAME"
    content += "\n"

    content += f"{address_parts[2]}"
    content += f"{get_spaces(address_parts[2])}"
    content += "STREET_NAME"

    return content

def pattern_maker_single(c_line, pattern_index):

    if(pattern_index == 1):
        return pattern_1_maker_single(c_line)
    elif(pattern_index == 2):
        return pattern_2_maker_single(c_line)
    elif(pattern_index == 3):
        return pattern_3_maker_single(c_line)
    elif(pattern_index == 4):
        return pattern_4_maker_single(c_line)
    elif(pattern_index == 5):
        return pattern_5_maker_single(c_line)
    elif(pattern_index == 6):
        return pattern_6_maker_single(c_line)
    elif(pattern_index == 7):
        return pattern_7_maker_single(c_line)
    elif(pattern_index == 8):
        return pattern_8_maker_single(c_line)
    elif(pattern_index == 9):
        return pattern_9_maker_single(c_line)
    elif(pattern_index == 10):
        return pattern_10_maker_single(c_line)
    elif(pattern_index == 11):
        return pattern_11_maker_single(c_line)
    elif(pattern_index == 12):
        return pattern_12_maker_single(c_line)
    elif(pattern_index == 13):
        return pattern_13_maker_single(c_line)
    elif(pattern_index == 14):
        return pattern_14_maker_single(c_line)

    return 0

def pattern_maker_multiple(pattern_index):

    file = f'pattern{pattern_index}.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        content += pattern_maker_single(c_line, pattern_index)

        content += "\n\n"

    # print(content)

    return content

def startpy():
    
    # pattern_1_maker_single("12A WEST STREET")

    # Pattern 1
    # print(pattern_maker_multiple(1))

    # Pattern 2
    # print(pattern_maker_multiple(2))

    # Pattern 3
    # print(pattern_maker_multiple(3))

    # Pattern 4
    # print(pattern_maker_multiple(4))

    # Pattern 5
    # pattern_5_maker_single("1/3 WESTGATE PARK FODDERWICK")
    print(pattern_maker_multiple(5))

    # Pattern 6
    # print(pattern_maker_multiple(6))

    # Pattern 7
    # print(pattern_maker_multiple(7))

    # Pattern 8
    # print(pattern_maker_multiple(8))

    # Pattern 9
    # print(pattern_maker_multiple(9))

    # Pattern 10
    # print(pattern_maker_multiple(10))

    # Pattern 11
    # print(pattern_maker_multiple(11))

    # Pattern 12
    # print(pattern_maker_multiple(12))

    # Pattern 13
    # print(pattern_maker_multiple(13))

    # Pattern 14
    # print(pattern_maker_multiple(14))

    pass


if __name__ == '__main__':
    startpy()