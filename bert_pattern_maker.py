

from sklearn.model_selection import train_test_split
from importlib import import_module

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
            content += get_single_content(current_index, c_item, "HOUSE_NO")
        else:
            sub_parts = c_item.split(" ")

            for item in sub_parts:
                content += get_single_content(current_index, item, "STREET_NAME")

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
        content += get_single_content(current_index, c_item, "STREET_NAME")

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

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        c_line = c_line.lower()

        current_index += 1

        content += pattern_maker_single(current_index, c_line, pattern_index)

    return content

def get_current_index():

    with open('address_training_bert_2.csv', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]

        try:
            cu_index = int(last_line.split(CSV_DELIM)[0])
        except:
            return -1

        return cu_index
    
current_index = get_current_index()

def startpy():

    # pattern_1_maker_single("12A WEST STREET")

    # Pattern 1
    print(pattern_maker_multiple(1))

    # Pattern 2
    # print(pattern_maker_multiple(2))

    # Pattern 3
    # print(pattern_maker_multiple(3))

    # Pattern 4
    # print(pattern_maker_multiple(4))

    # Pattern 5
    # pattern_5_maker_single("1/3 WESTGATE PARK FODDERWICK")
    # print(pattern_maker_multiple(5))

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

    # Pattern 15
    # print(pattern_maker_multiple(15))

    # Pattern 16
    # print(pattern_maker_multiple(16))

    # Pattern 17
    # print(pattern_maker_multiple(17))

    # Pattern 18
    # print(pattern_maker_multiple(18))

    # Pattern 19
    # print(pattern_maker_multiple(19))

    # print(pattern_21_maker_single("KAMPUNG MUHHIBAH 14981 JALAN PUCHONG"))
    # Pattern 21
    # print(pattern_maker_multiple(21))

    # Pattern 22
    # print(pattern_maker_multiple(22))

    # Pattern 23
    # print(pattern_maker_multiple(23))

    # Pattern 24
    # print(pattern_maker_multiple(24))

    # Pattern 26
    # print(pattern_maker_multiple(26))

    # Pattern 27
    # print(pattern_27_maker_single("76 W HORIZON RIDGE PKWY STE 120"))
    # print(pattern_maker_multiple(27))

    # Pattern 28
    # print(pattern_maker_multiple(28))

    # Pattern 29
    # print(pattern_maker_multiple(29))

    # Pattern 30
    # print(pattern_maker_multiple(30))

    # Pattern 31
    # print(pattern_maker_multiple(30))

    # Pattern 32
    # print(pattern_maker_multiple(32))

    # print(pattern_1_maker_single(current_index, "12A WEST STREET"))

    pass

if __name__ == '__main__':
    startpy()
