

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

def get_details_1():

    return fake.first_name(), fake.city()

def startpy():

    print(get_details_1())

if __name__ == '__main__':
    startpy()