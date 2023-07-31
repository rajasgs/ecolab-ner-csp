




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

java_file   = "SimplePredictNER.java"

jc_cmd      = 'javac -cp "jars/*" SimplePredictNER.java ' + java_file + ';'

cmd         = jc_cmd + 'java -cp "jars/*:." SimplePredictNER.java '


def get_tokens(address):

    address = address.replace("'", "")
    address = address.replace("&", "and")

    INPUT = address.replace("'", "")

    s = subprocess.check_output(
        cmd + INPUT,
        shell=True,
    )

    result = s.decode("utf-8")
    # result = result.strip('').replace('\n', '').strip()

    # result = result[1:]
    # result = result[:-1]

    result_parts = result.split('\n')[:-1]

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
    
    # result = get_tokens("152 ST ANNE'S RD")
    # print(result)

    # return

    df = pd.read_csv('ver-2023-01_test.csv')

    street_name_list = []
    house_no_list = []
    suite_no_list = []
    for index, row in df.iterrows():
        # print(f'{index} : {row["ADDRESS"]}')

        token_dict = get_tokens(row["ADDRESS"])

        street_name_list.append(token_dict['STREET_NAME'])
        house_no_list.append(token_dict['HOUSE_NO'])
        suite_no_list.append(token_dict['SUITE_NO'])

    df.insert(3,'STREET_NAME', street_name_list)
    df.insert(4,'HOUSE_NO', house_no_list)
    df.insert(5,'SUITE_NO', suite_no_list)

    df.to_csv('ver-2023-01_test2_output.csv', index=False)

    _secs = (datetime.now() - start_time).total_seconds()
    print('Time : ', _secs)

if __name__ == '__main__':
    startpy()