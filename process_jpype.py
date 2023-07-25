




'''
Created on 

@author: Raja CSP Raman

source:
    
'''


import os
import subprocess

import pandas as pd
import random
from datetime import datetime
import jpype

def get_tokens(address):

    

    SampleClass = jpype.JClass("SimplePredictNER")

    # address = address.replace("'", "")
    # address = address.replace("&", "and")

    # INPUT = address.replace("'", "")

    result = SampleClass.getTokens(str(address))

    # print(result)

    result_parts = result.split('\n')

    street_name = result_parts[0].replace('STREET_NAME=', '')
    house_no    = result_parts[1].replace('HOUSE_NO=', '')
    suite_no    = result_parts[2].replace('SUITE_NO=', '')

    # print(f"{street_name}")
    # print(f"{house_no}")
    # print(f"{suite_no}") 

    token_dict = {
        'STREET_NAME'   : street_name,
        'HOUSE_NO'      : house_no,
        'SUITE_NO'      : suite_no,
    }

    return token_dict

def get_random_entry(part):

    return f'{part}_{random.randint(1, 1000)}'

def startpy():

    start_time = datetime.now()

    jpype.startJVM(classpath = ['jars/*', "/home/rajaraman/rprojects/ecolab-ner-csp/"])
    
    # result = get_tokens("152 ST ANNE'S RD")
    # print(result)

    # return

    df = pd.read_csv('ver-2023-01_test.csv')

    street_name_list    = []
    house_no_list       = []
    suite_no_list       = []

    street_name_right_list    = []
    house_no_right_list       = []
    suite_no_right_list       = []
    for index, row in df.iterrows():
        # print(f'{index} : {row["ADDRESS"]}')

        address_token_dict = get_tokens(row["ADDRESS"])

        street_name_list.append(address_token_dict['STREET_NAME'])
        house_no_list.append(address_token_dict['HOUSE_NO'])
        suite_no_list.append(address_token_dict['SUITE_NO'])

        address_right_token_dict = get_tokens(row["ADDRESS_RIGHT"])

        street_name_right_list.append(address_right_token_dict['STREET_NAME'])
        house_no_right_list.append(address_right_token_dict['HOUSE_NO'])
        suite_no_right_list.append(address_right_token_dict['SUITE_NO'])

    df.insert(8,'STREET_NAME_RIGHT', street_name_right_list)
    df.insert(9,'HOUSE_NO_RIGHT', house_no_right_list)
    df.insert(10,'SUITE_NO_RIGHT', suite_no_right_list)

    df.insert(3,'STREET_NAME', street_name_list)
    df.insert(4,'HOUSE_NO', house_no_list)
    df.insert(5,'SUITE_NO', suite_no_list)

    df.to_csv('ver-2023-01_test_output.csv', index=False)

    _secs = (datetime.now() - start_time).total_seconds()
    print('Time : ', _secs)

if __name__ == '__main__':
    startpy()