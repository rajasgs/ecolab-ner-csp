


# import validator_single_extended as vase
import pandas as pd
from constants import *

import jpype

jpype.startJVM(classpath    = ['jars/*', "./"])

def test_single(c_address, model_path):

    simple_predict_class        = jpype.JClass("SimplePredictNERNoSingleton")

    result = simple_predict_class.getTokens(str(c_address), model_path)

    result_parts = result.split('\n')

    street_name = result_parts[0].replace('STREET_NAME=', '')
    house_no    = result_parts[1].replace('HOUSE_NO=', '')
    suite_no    = result_parts[2].replace('SUITE_NO=', '')

    if(suite_no == 'null'):
        suite_no = 'null'

    token_dict = {
        "STREET_NAME"   : str(street_name),
        "HOUSE_NO"      : str(house_no),
        "SUITE_NO"      : str(suite_no),
    }

    return token_dict

def print_addres_dict(c_dict):

    for key, val in c_dict.items():
        print(f"{key}: {val}")

def startpy():

    import sys

    model_name = sys.argv[1]
    c_address = sys.argv[2]

    print(f"c_address: {c_address}")

    result = test_single(c_address, model_name)
    print_addres_dict(result)

    pass

if __name__ == '__main__':
    
    startpy()

    # test_java_class()



    pass
'''
How to run?

python predict_single.py /home/rajaraman/datasets/ecolab-ner-archive/ecolab_address_20240308_1.model.ser.gz "12-89 spadina road"
'''