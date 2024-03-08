


import validator_single_extended as vase
import pandas as pd
from constants import *

import jpype

def test_single(c_address, model_path):

    vas_singleton = vase.ValidatorSingletonExtended.getInstance(model_path = f"{model_path}")

    result = vas_singleton.get_tokens(c_address)

    return result

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

def test_java_class():

    java_class        = jpype.JClass("ClassA")

    java_class.hello()
    
if __name__ == '__main__':
    
    startpy()

    # test_java_class()



    pass
'''
How to run?

python predict_single.py /home/rajaraman/datasets/ecolab-ner/ecolab_address_20240308_1.model.ser.gz "12-89 spadina road"
'''