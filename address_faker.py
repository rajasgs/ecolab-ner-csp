




'''
Created on 

@author: Raja CSP Raman

source:
    https://faker.readthedocs.io/en/master/locales/de_DE.html  

    https://faker.readthedocs.io/en/master/locales/en_IN.html?highlight=india#faker.providers.address.en_IN.Provider.current_country
    https://faker.readthedocs.io/en/master/locales/en_CA.html?highlight=canada 


    en_IN
'''

from faker import Faker

def startpy():
    pass

    fake = Faker('en_CA')

    # Faker.seed(0)
    for _ in range(5):
        print(fake.street_address(), '\n')

if __name__ == '__main__':
    startpy()