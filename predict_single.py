


import validator_single_extended as vase
import pandas as pd
from constants import *

vas_singleton = vase.ValidatorSingletonExtended.getInstance(model_path = f"{CORE_NLP_MODELNAME}.model.ser.gz")

def test_single(c_address):

    predicted = vas_singleton.get_tokens(c_address)
    print(predicted)

    return predicted

def startpy():

    import sys

    c_address = sys.argv[1]

    test_single(c_address)

    pass

if __name__ == '__main__':
    startpy()


'''
How to run?

python predict_single.py "12-89 spadina road"
'''