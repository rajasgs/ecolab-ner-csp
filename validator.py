
'''
Created on 

@author: Raja CSP Raman

source:
    

address,street_name_original,house_no_original,suite_no_original,street_name_predicted,house_no_predicted,suite_no_predicted,predicted_right


address
street_name_original
house_no_original
suite_no_original
street_name_predicted
house_no_predicted
suite_no_predicted
predicted_right
'''

import jpype
import dataframe_util as du
import faker_util as fu

MODEL_PATH = "ecolab_address_20230817.model.ser.gz"

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
    }

    return token_dict

def singleton_test(filename):

    singleton_class = jpype.JClass("SingletonTest")

    singleton_instance = singleton_class.getInstance("two.txt")
    singleton_instance.printFilename()


def add_dummy_original_address():

    address, street_name, house_no, suite_no = fu.create_address_pattern_30()

    du.append_original_to_csv(
        address = address,
        street_name_original= street_name,
        house_no_original= house_no,
        suite_no_original= suite_no
    )

    print(f'Added : {address}')


singleton_predict = None

def initiate():

    global singleton_predict

    jpype.startJVM(classpath = ['jars/*', "./"])
    simple_predict_class = jpype.JClass("SimplePredictNER")
    singleton_predict = simple_predict_class.getInstance(MODEL_PATH)

def fill_addresses(limit = 5):

    for _index in range(limit):
        add_dummy_original_address()

def predict_single_address_with_model(c_index):

    c_row = du.get_row(c_index)

    # print(c_row)
    # print(type(c_row))

    c_address               = c_row['address']
    c_street_name_original  = c_row['street_name_original']
    c_house_no_original     = c_row['house_no_original']
    c_suite_no_original     = c_row['suite_no_original']

    print(f'address         : {c_address} \
          \n \
          \nstreet_name_o   : {c_street_name_original} \
          \nhouse_no_o      : {c_house_no_original} \
          \nsuite_no_o      : {c_suite_no_original} \
    ')

    address_dict = get_tokens(singleton_predict, c_address)

    c_street_name_predicted  = address_dict['STREET_NAME']
    c_house_no_predicted     = address_dict['HOUSE_NO']
    c_suite_no_predicted     = address_dict['SUITE_NO']

    print(f' \
          \nstreet_name_p   : {c_street_name_predicted} \
          \nhouse_no_p      : {c_house_no_predicted} \
          \nsuite_no_p      : {c_suite_no_predicted} \
    ')

    print(f'\n')

    du.fill_predicted(
        c_index,

        c_street_name_predicted,
        c_house_no_predicted,
        c_suite_no_predicted,
    )

def startpy():

    initiate()
    
    # fill_addresses(10)

    # return

    df = du.get_df()

    for idx in range(len(df)):
        print(f'idx : {idx}')
        predict_single_address_with_model(idx)    
    
    # print(get_tokens(singleton_predict, "152 ST ANNE'S RD"))
    # print(get_tokens(singleton_predict, "254 Spadina Road"))

    # print(singleton_test("one.txt"))

    # singleton_test("two.txt")

if __name__ == '__main__':
    startpy()