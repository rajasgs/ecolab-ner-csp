
'''

Created on 

@author: Raja CSP Raman

source:
    
'''

def pattern_1_maker(address):

    '''
        12A WEST STREET
    '''

    address_parts = address.split(" ")

    content = f"""
{address_parts[0]}      HOUSE_NO
{address_parts[1]}      STREET_NAME
{address_parts[2]}      STREET_NAME  
    """

    print(content)

def startpy():
    
    pattern_1_maker("12A WEST STREET")



if __name__ == '__main__':
    startpy()