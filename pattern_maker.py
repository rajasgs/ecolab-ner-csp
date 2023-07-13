
'''

Created on 

@author: Raja CSP Raman

source:
    
    Address-CNER
    https://docs.google.com/spreadsheets/d/1QH_T6C3MAJNj5f_1gL1dZtLRUjFbwJ4wcHpPwlCfylI/edit#gid=968221325
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

def pattern_1_maker_multiple():

    file = 'pattern1.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        content += pattern_1_maker_single(c_line)

        content += "\n\n"

    # print(content)

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

    content += f"-{sub_parts[1]}"
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

def pattern_3_maker_multiple():

    file = 'pattern3.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        content += pattern_3_maker_single(c_line)

        content += "\n\n"

    # print(content)

    return content

def startpy():
    
    # pattern_1_maker_single("12A WEST STREET")

    # Pattern 1
    # print(pattern_1_maker_multiple())

    # Pattern 3
    # print(pattern_3_maker_single("1626-1630 NESS AVE"))
    print(pattern_3_maker_multiple())

    # Pattern 3
    # print(pattern_3_maker_single("1626-1630 NESS AVE"))
    # print(pattern_3_maker_multiple())

    pass


if __name__ == '__main__':
    startpy()