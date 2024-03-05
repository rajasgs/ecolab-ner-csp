


import validator_single_extended as vase
import pandas as pd
from constants import *

import jpype

jpype.startJVM(classpath    = ['jars/*', "./"])

# vas_singleton = vase.ValidatorSingletonExtended.getInstance(model_path = f"{CORE_NLP_MODELNAME}.model.ser.gz")

def test_single(c_address, model_name):

    if("ecolab_".startswith(model_name)):
        model_name = f"ecolab_{model_name}"

    model_path = f"{model_name}.model.ser.gz"

    simple_predict_class        = jpype.JClass("SimplePredictNERNoSingleton")

    predicted = simple_predict_class.getTokens(c_address, model_name)
    print(predicted)

    return predicted

def startpy():

    import sys

    model_name = "ecolab_address_20230828_3"
    c_address = sys.argv[2]

    test_single(c_address, model_name)

    pass

def test_java_class():

    java_class        = jpype.JClass("ClassA")

    java_class.hello()
    
if __name__ == '__main__':
    # startpy()

    test_java_class()



    pass
'''
How to run?

python predict_single.py ecolab_address_20240103_1 "12-89 spadina road"
'''