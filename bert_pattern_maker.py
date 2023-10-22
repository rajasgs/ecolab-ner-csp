

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

def pattern_maker_single(current_index, c_line, pattern_index):

    dynamic_module  = import_module(f"bert_pattern_maker")
    dynamic_method  = getattr(dynamic_module, f"pattern_{pattern_index}_maker_single")

    return dynamic_method(current_index, c_line)

def pattern_maker_multiple(current_index, pattern_index):

    file = f'{PATTERNS_FOLDER}pattern{pattern_index}.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    # train_list, test_list = train_test_split(lines, train_size=0.8)

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        c_line = c_line.lower()

        current_index += 1

        content += pattern_maker_single(current_index, c_line, pattern_index)

        # content += "\n"

    # content += str("\n")

    # for c_line in test_list:
    #     c_line = c_line.replace('\n', '')

    #     c_line = c_line.lower()

    #     current_index += 1

    #     content += pattern_maker_single(current_index, c_line, pattern_index)

    #     # content += "\n"

    # print(content)

    return content


def startpy():

    current_index = 136
    
    # pattern_1_maker("545 N ALBERT ST") #-> fixed
    print(pattern_maker_multiple(current_index, 1))

    

    # print(pattern_1_maker_single(current_index, "12A WEST STREET"))

    pass

if __name__ == '__main__':
    startpy()
