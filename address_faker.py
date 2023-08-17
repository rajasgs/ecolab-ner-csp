




'''
Created on 

@author: Raja CSP Raman

source:
    https://faker.readthedocs.io/en/master/locales/de_DE.html  

    https://faker.readthedocs.io/en/master/locales/en_IN.html?highlight=india#faker.providers.address.en_IN.Provider.current_country
    https://faker.readthedocs.io/en/master/locales/en_CA.html?highlight=canada 

    Address-CNER
    https://docs.google.com/spreadsheets/d/1QH_T6C3MAJNj5f_1gL1dZtLRUjFbwJ4wcHpPwlCfylI/edit#gid=968221325

    en_IN
'''

from faker import Faker

fake = Faker('en_CA')

MAX_LIMIT = 200

def create_address_pattern_30():

    house_no        =  fake.building_number()
    street_name     = fake.street_name()

    address = f"{street_name} {house_no}"

    return address

def startpy():

    pass

    # Faker.seed(0)
    for _ in range(MAX_LIMIT):
        # print(fake.street_address(), '\n')
        print(create_address_pattern_30())

if __name__ == '__main__':
    startpy()