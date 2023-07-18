
'''

Created on 

@author: Raja CSP Raman

source:
    
    Address-CNER
    https://docs.google.com/spreadsheets/d/1QH_T6C3MAJNj5f_1gL1dZtLRUjFbwJ4wcHpPwlCfylI/edit#gid=968221325

    https://www.kaggle.com/rajacsp/address-pattern/

    https://stackoverflow.com/questions/31627321/testing-if-a-value-is-numeric

    
'''

import numbers

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

    content += get_single_content(address_parts[0], "HOUSE_NO")
    content += get_single_content(address_parts[1], "STREET_NAME")
    content += get_single_content(address_parts[2], "STREET_NAME")

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
        content += get_single_content(c_item, "STREET_NAME")

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

            content += get_single_content(sub_parts[0], "SUITE_NO")
            content += get_single_content(sub_parts[1], "HOUSE_NO")

        else:
            content += get_single_content(c_item, "STREET_NAME")

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


    content += get_single_content(sub_parts[0], "SUITE_NO")
    content += get_single_content("-", "0")
    content += get_single_content(sub_parts[1], "HOUSE_NO")

    content += get_single_content(address_parts[1], "STREET_NAME")
    content += get_single_content(address_parts[2], "STREET_NAME")

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

            content += get_single_content(sub_parts[0], "SUITE_NO")
            content += get_single_content("-", "0")
            content += get_single_content(sub_parts[1], "HOUSE_NO")
        else:
            content += get_single_content(c_item, "STREET_NAME")

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
                content += get_single_content(c_item, "SUITE_NO")
            else:
                content += get_single_content(c_item, "STREET_NAME")

        else:
            content += get_single_content(c_item, "STREET_NAME")
        
    
    content += get_single_content("#", "0")
    content += get_single_content(address_full_parts[1], "0")

    return content


def pattern_7_maker_single(address):

    '''
        Pattern 7:
        
        7	
        (StreetName) (Suite_No) (StreetName)	        

        Sample:
        BOTANY TOWN CENTRE 588 CHAPEL ROAD

        Not clear
    '''

    pass

def pattern_8_maker_single(address):

    '''
        Pattern :

        

        Sample:
        

        Not clear
    '''

    pass

def pattern_9_maker_single(address):

    '''
        Pattern :

        

        Sample:
        
        Not clear
    '''

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

    content += get_single_content(address_parts[0], "HOUSE_NO")
    content += get_single_content(address_parts[1], "STREET_NAME")
    content += get_single_content(address_parts[2], "STREET_NAME")

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

            content += get_single_content(sub_parts[0], "SUITE_NO")
            content += get_single_content("-", "0")
            content += get_single_content(sub_parts[1], "HOUSE_NO")

        else:
            content += get_single_content(c_item, "STREET_NAME")

    return content

def pattern_12_maker_single(address):

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
            content += get_single_content(c_item, "SUITE_NO")

        elif(c_index == 1):

            content += get_single_content(c_item, "HOUSE_NO")

        else:
            content += get_single_content(c_item, "STREET_NAME")


    # print(content)

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

    content += get_single_content(address_parts[0], "HOUSE_NO")
    content += get_single_content(address_parts[1], "STREET_NAME")
    content += get_single_content(address_parts[2], "STREET_NAME")
    content += get_single_content(address_parts[3], "SUITE_NO")
    content += get_single_content(address_parts[4], "SUITE_NO")

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

    content += get_single_content(address_parts[0], "HOUSE_NO")
    content += get_single_content(address_parts[1], "STREET_NAME")
    content += get_single_content(address_parts[2], "STREET_NAME")

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
            content += get_single_content(c_item, "HOUSE_NO")

        else:
            content += get_single_content(c_item, "STREET_NAME")

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
            content += get_single_content(c_item, "HOUSE_NO")
        else:
            content += get_single_content(c_item, "STREET_NAME")

    return content


def pattern_17_maker_single(address):

    '''
        Pattern 17:

        17	
        ( Street_No) (Street_Name) (Post_Box_No)	
        

        Sample:
        99 LEVEN STREET PO BOX 7159

        
    '''

    main_address_parts = address.split("PO BOX")

    address_parts = main_address_parts[0].split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        c_item = c_item.strip()

        if(len(c_item) == 0):
            continue

        if(c_index == 0):
            content += get_single_content(c_item, "HOUSE_NO")
        else:
            content += get_single_content(c_item, "STREET_NAME")

    content += get_single_content("PO BOX", "HOUSE_NO")

    sub_address = main_address_parts[1].strip()
    content += get_single_content(sub_address, "HOUSE_NO")

    return content

def pattern_18_maker_single(address):

    '''
        Pattern 17:

        18		

        Sample:
        103 PTH 12 N

        
    '''

    pass


def pattern_19_maker_single(address):

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
            content += get_single_content(c_item, "HOUSE_NO")
        else:
            content += get_single_content(c_item, "STREET_NAME")

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
            content += get_single_content(c_item, "HOUSE_NO")
            break
        
        content += get_single_content(c_item, "SUITE_NO")

    # print(content)

    for c_index, c_item in enumerate(ad_list):

        if(c_index > int_index):
            content += get_single_content(c_item, "STREET_NAME")

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
            content += get_single_content(c_item, "HOUSE_NO")

            break
        
        content += get_single_content(c_item, "STREET_NAME")

    return content


def pattern_23_maker_single(address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''
    
    pass


def pattern_24_maker_single(address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''

    

    # print(content)

    pass


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
            content += get_single_content(c_item, "SUITE_NO")
        else:
            if(c_index == 2 and is_int(c_item)):
                content += get_single_content(c_item, "HOUSE_NO")
                after_suite_flag = True
            else:
                content += get_single_content(c_item, "STREET_NAME")
    # print(content)

    return content
    

    # print(content)

    pass


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
            content += get_single_content(c_item, "HOUSE_NO")
        else:

            if(c_item == "STE" or c_item == "SUITE"):
                content += get_single_content(c_item, "SUITE_NO")

                after_suite_flag = True
            else:

                if(after_suite_flag):
                    content += get_single_content(c_item, "SUITE_NO")
                else:
                    content += get_single_content(c_item, "STREET_NAME")

    # print(content)

    return content

def pattern_28_maker_single(address):

    '''
        Pattern 17:

        

        Sample:
        

        
    '''

    address_parts = address.split(" ")

    content = ""

    for c_index, c_item in enumerate(address_parts):
        # print(c_index, c_item)

        if(c_index == 0):
            content += get_single_content(c_item, "HOUSE_NO")
        else:
            content += get_single_content(c_item, "STREET_NAME")

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
            content += get_single_content(c_item, "HOUSE_NO")
        else:
            content += get_single_content(c_item, "STREET_NAME")

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
    elif(pattern_index == 15):
        return pattern_15_maker_single(c_line)
    elif(pattern_index == 16):
        return pattern_16_maker_single(c_line)
    elif(pattern_index == 17):
        return pattern_17_maker_single(c_line)
    elif(pattern_index == 19):
        return pattern_19_maker_single(c_line)
    elif(pattern_index == 21):
        return pattern_21_maker_single(c_line)
    elif(pattern_index == 22):
        return pattern_22_maker_single(c_line)
    elif(pattern_index == 26):
        return pattern_26_maker_single(c_line)
    elif(pattern_index == 27):
        return pattern_27_maker_single(c_line)
    elif(pattern_index == 28):
        return pattern_28_maker_single(c_line)
    elif(pattern_index == 29):
        return pattern_29_maker_single(c_line)

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
    print(pattern_maker_multiple(11))

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

    # Pattern 19
    # print(pattern_maker_multiple(19))

    # print(pattern_21_maker_single("KAMPUNG MUHHIBAH 14981 JALAN PUCHONG"))
    # Pattern 21
    # print(pattern_maker_multiple(21))

    # Pattern 22
    # print(pattern_maker_multiple(22))

    # Pattern 26
    # print(pattern_maker_multiple(26))

    # Pattern 27
    # print(pattern_27_maker_single("76 W HORIZON RIDGE PKWY STE 120"))
    # print(pattern_maker_multiple(27))

    # Pattern 28
    # print(pattern_maker_multiple(28))

    # Pattern 29
    # print(pattern_maker_multiple(29))

    pass


if __name__ == '__main__':
    startpy()



'''
Status:

Total Done:

Can't do:
2?


01 - DONE

02 - DONE

03 - DONE

04 - DONE

05 - DONE

06 - DONE 

07 - CANT DO

08 - CANT DO

09 - CANT DO

10 - DONE

11 - DONE

12 - DONE

13 - DONE

14 - DONE

15 - DONE

16 - DONE

17 - DONE

18

19 - DONE

20

21 - DONE

22 - DONE

23

24

25 - CAN'T DO

26 - DONE

27 - DONE

28 - DONE

29 - DONE

'''