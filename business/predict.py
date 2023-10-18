

import jpype

MODEL_PATH = "ecolab_address_20230828_3.model.ser.gz"

singleton_predict = None

def initiate():

    global singleton_predict

    jpype.startJVM(classpath = ['jars/*', "./"])
    simple_predict_class = jpype.JClass("SimplePredictNER")
    singleton_predict = simple_predict_class.getInstance(MODEL_PATH)

def get_tokens(singleton_predict, address):

    result = singleton_predict.getTokens(str(address))

    # print(result)

    result_parts = result.split('\n')

    street_name = result_parts[0].replace('STREET_NAME=', '')
    house_no    = result_parts[1].replace('HOUSE_NO=', '')
    suite_no    = result_parts[2].replace('SUITE_NO=', '')

    token_dict = {
        'STREET_NAME'   : street_name,
        'HOUSE_NO'      : house_no,
        'SUITE_NO'      : suite_no,
        'FULL'          : result
    }

    return token_dict

def predict(c_address):

    address_dict = get_tokens(singleton_predict, c_address)

    print(f'address_dict : {address_dict}')

    return address_dict