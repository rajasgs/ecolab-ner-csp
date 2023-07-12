
'''

Created on 

@author: Raja CSP Raman

source:
    
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


def pattern_2_maker_single(address):

    '''
        1626-1630   SUITE_AND_HOUSE_NO
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

def pattern_2_maker_multiple():

    file = 'pattern2.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        content += pattern_2_maker_single(c_line)

        content += "\n\n"

    # print(content)

    return content

def startpy():
    
    # pattern_1_maker_single("12A WEST STREET")

    # content = pattern_1_maker_multiple()
    # # print(content)

    # 1626-1630 NESS AVE
    # print(pattern_2_maker_single("1626-1630 NESS AVE"))

    print(pattern_2_maker_multiple())

    pass


if __name__ == '__main__':
    startpy()