
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
import json_util as ju

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

    ju.add_address_base(
        address, 
        street_name, 
        house_no, 
        suite_no
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

def isNaN(num):
    return num != num

def convert_2(content):

    if(not content):
        return content
    
    if(isNaN(content)):
        return content
    
    if('null' == content):
        return content
    
    if(None == content):
        return content
    
    if('None' == content):
        return content

    return str(content)

def is_predicted_right(
    c_street_name_original,
    c_house_no_original,
    c_suite_no_original,

    c_street_name_predicted,
    c_house_no_predicted,
    c_suite_no_predicted
):
    
    if(c_street_name_original != c_street_name_predicted):
        return 0
    
    c_house_no_original = convert_2(c_house_no_original)
    c_house_no_predicted = convert_2(c_house_no_predicted)

    c_suite_no_original = convert_2(c_suite_no_original)
    c_suite_no_predicted = convert_2(c_suite_no_predicted)
    
    # print(f'c_house_no_original : {c_house_no_original} type : {type(c_house_no_original)}, \
    #       c_house_no_predicted : {c_house_no_predicted} type : {type(c_house_no_predicted)}')
    
    if(c_house_no_original != c_house_no_predicted):
        return 0
    
    # print(f'c_suite_no_original : {c_suite_no_original}, type : {type(c_suite_no_original)} \
    #       ')
    # if(c_suite_no_original != c_suite_no_predicted):
    #     return 0

    return 1

def convert_data(content):

    if(not content):
        return content
    
    if(content == 'null'):
        return content
    
    return (str(content))

def predict_single_address_with_model(entry):

    c_address               = entry['address']
    c_street_name_original  = entry['street_name_original']
    c_house_no_original     = entry['house_no_original']
    c_suite_no_original     = entry['suite_no_original']

    print(f'address         : {c_address} \
          \n \
          \nstreet_name_o   : {c_street_name_original} \
          \nhouse_no_o      : {c_house_no_original} \
          \nsuite_no_o      : {c_suite_no_original} \
    ')

    address_dict = get_tokens(singleton_predict, c_address)

    print(f'address_dict : {address_dict}')

    # c_street_name_predicted  = str(address_dict['STREET_NAME'])
    # c_house_no_predicted     = convert_data(address_dict['HOUSE_NO'])
    # c_suite_no_predicted     = convert_data(address_dict['SUITE_NO'])

    c_street_name_predicted  = str(address_dict['STREET_NAME'])
    c_house_no_predicted     = convert_data(address_dict['HOUSE_NO'])
    c_suite_no_predicted     = ''

    print(f' \
          \nstreet_name_p   : {c_street_name_predicted} \
          \nhouse_no_p      : {c_house_no_predicted} \
          \nsuite_no_p      : {c_suite_no_predicted} \
    ')

    print(f'\n')

    predicted = is_predicted_right(
        c_street_name_original,
        c_house_no_original,
        c_suite_no_original,

        c_street_name_predicted,
        c_house_no_predicted,
        c_suite_no_predicted
    )

    dict_2 = {
        "address" : c_address,
        
        "street_name_original" : c_street_name_original,
        "house_no_original" : c_house_no_original,
        "suite_no_original" :  c_suite_no_original,

        "street_name_predicted" : c_street_name_predicted,
        "house_no_predicted" : c_house_no_predicted,
        "suite_no_predicted" : c_suite_no_predicted,

        "predicted_right" : predicted
    }

    return dict_2



def startpy():

    initiate()
    
    # fill_addresses(2)

    # return

    # df = du.get_df()

    data = ju.get_json_data()

    new_data = {
        'entries' : []
    }

    for idx, entry in enumerate(data['entries']):
        print(entry)
        # print(f'idx : {idx}')
        new_dict = predict_single_address_with_model(entry)  

        new_data['entries'].append(new_dict)

    ju.update_all(new_data)

    # print(get_tokens(singleton_predict, "152 ST ANNE'S RD"))
    # print(get_tokens(singleton_predict, "254 Spadina Road"))

    # print(singleton_test("one.txt"))

    # singleton_test("two.txt")

    pass

if __name__ == '__main__':
    startpy()