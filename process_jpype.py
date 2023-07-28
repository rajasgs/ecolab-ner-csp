




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

FROM_FILE   = 'ver-2023-01_train.csv'
TO_FILE     = 'ver-2023-01_train_output_20230728.csv'

# FROM_FILE   = 'International Addresses with Premise number.csv'
# TO_FILE     = 'International Addresses with Premise number output.csv'

def get_tokens(singleton_predict, address):

    

    # SampleClass = jpype.JClass("SimplePredictNER")

    # address = address.replace("'", "")
    # address = address.replace("&", "and")

    # INPUT = address.replace("'", "")

    result = singleton_predict.getTokens(str(address))

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

    # jpype.startJVM(classpath = ['jars/*', "./"])

    jpype.startJVM(classpath = ['jars/*', "./"])
    simple_predict_class = jpype.JClass("SimplePredictNER")
    singleton_predict = simple_predict_class.getInstance("Ecolab_address_ner_model_Ver2.model.ser.gz")
    
    # result = get_tokens("152 ST ANNE'S RD")
    # print(result)

    # return

    df = pd.read_csv(FROM_FILE)

    street_name_list    = []
    house_no_list       = []
    suite_no_list       = []

    street_name_right_list    = []
    house_no_right_list       = []
    suite_no_right_list       = []
    for index, row in df.iterrows():
        # print(f'{index} : {row["ADDRESS"]}')

        # Option 1
        address_token_dict = get_tokens(singleton_predict, row["ADDRESS"])

        street_name_list.append(address_token_dict['STREET_NAME'])
        house_no_list.append(address_token_dict['HOUSE_NO'])
        suite_no_list.append(address_token_dict['SUITE_NO'])

        address_right_token_dict = get_tokens(singleton_predict, row["ADDRESS_RIGHT"])

        street_name_right_list.append(address_right_token_dict['STREET_NAME'])
        house_no_right_list.append(address_right_token_dict['HOUSE_NO'])
        suite_no_right_list.append(address_right_token_dict['SUITE_NO'])


        # option 2
        # address_token_dict = get_tokens(row["Address Line 1 Cleansed"])

        # street_name_list.append(address_token_dict['STREET_NAME'])
        # house_no_list.append(address_token_dict['HOUSE_NO'])
        # suite_no_list.append(address_token_dict['SUITE_NO'])

        if(index % 50 == 0):
            print(f'Reached {index}')

    df.insert(8,'STREET_NAME_RIGHT', street_name_right_list)
    df.insert(9,'HOUSE_NO_RIGHT', house_no_right_list)
    df.insert(10,'SUITE_NO_RIGHT', suite_no_right_list)

    df.insert(2,'STREET_NAME', street_name_list)
    df.insert(3,'HOUSE_NO', house_no_list)
    df.insert(4,'SUITE_NO', suite_no_list)

    df.to_csv(TO_FILE, index=False)

    _secs = (datetime.now() - start_time).total_seconds()
    print('Time : ', _secs)

if __name__ == '__main__':
    startpy()