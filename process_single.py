




'''
Created on 

@author: Raja CSP Raman

source:
    
'''


import os
import subprocess

import pandas as pd


java_file   = "SimplePredictNER.java"

jc_cmd      = "javac -cp 'jars/*' SimplePredictNER.java " + java_file + ";"

cmd         = jc_cmd + "java -cp 'jars/*:.' SimplePredictNER.java "


def get_tokens(address):

    INPUT = address

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

def startpy():
    
    result = get_tokens('1980 Rue St Patrice E')
    print(result)

    df = pd.read_csv('ver-2023-01_test.csv')

if __name__ == '__main__':
    startpy()