

'''
Created on 

@author: Raja CSP Raman

source:
    
'''

from faker import Faker

fake = Faker('en_CA')

MAX_LIMIT = 80

def create_address_pattern_30():

    house_no        = fake.building_number()
    street_name     = fake.street_name()

    suite_no        = None

    address = f"{street_name} {house_no}"

    return address, street_name, house_no, suite_no
