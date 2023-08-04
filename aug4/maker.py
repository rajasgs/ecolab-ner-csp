
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

def get_single_content(item, tag):

    item = item.lower()

    content = ""

    content += f"{item}"
    content += f"{get_spaces(item)}"
    content += f"{tag}"
    content += "\n"

    return content

def pattern_maker_multiple(file):

    # file = f'pattern{pattern_index}.txt'

    lines = None
    with open(file) as f:
        lines = f.readlines()

    # print(lines)

    content = ""

    for c_line in lines:
        c_line = c_line.replace('\n', '')

        # content += pattern_maker_single(c_line, pattern_index)

        for c_item in c_line.split(" "):
            # content += c_item
            content += get_single_content(c_item, "0")
            # content += "\n"

        content += "\n\n"

    print(content)

    return content


def startpy():

    pattern_maker_multiple('testing/raja_testing_aug_4.txt')



if __name__ == '__main__':
    startpy()