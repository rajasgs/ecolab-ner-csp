

'''

'''

import validator_single_extended as vase
import pandas as pd
from constants import *
import sys

FILEPATH = TESTING_FILEPATH

COL_ADDRESS =  'address_standardized'

TESTING_SHEET = 'testing-unique'
TESTING_SHEET = 'testing'

vas_singleton = None
if(len(sys.argv) == 2):
    mpath = sys.argv[1]
    vas_singleton = vase.ValidatorSingletonExtended.getInstance(model_path = f"{mpath}")
else:
    vas_singleton = vase.ValidatorSingletonExtended.getInstance(model_path = f"{FINEL_NER_MODEL_BASE}{CORE_NLP_MODELNAME}.model.ser.gz")

def is_unncessary_column(col_name):

    if("Unnamed:" in col_name):
        return True

    return False

def read_addess_full_excel():

    # Replace 'path_to_file.xlsx' with the path to your Excel file
    df = pd.read_excel(
        FILEPATH, 
        sheet_name=TESTING_SHEET, 
        engine='openpyxl', 
        header = 1,
        converters={'suite_no':str}
    )

    return df

# def read_addess_full_csv():

#     df = df.read_csv("Address-Patterns-RS-address-ner-testing-20240229-1.csv", header=1)

#     return df

def read_address_csv():

    df = read_addess_full_excel()

    col_list = df.columns.tolist()

    unnecessary_cols = []

    for c_col in col_list:
        if(is_unncessary_column(c_col)):
            unnecessary_cols.append(unnecessary_cols)
            df = df.drop(c_col, axis=1)

    col_list = df.columns.tolist()

    # print(f'col_list : {col_list}')

    df.dropna()

    # df = df[0:MAX_READ_ROWS]

    return df

def classify_address(
    address
):
    

    result = vas_singleton.get_tokens(address)
    print(f'result : {result}')

    print(f'vas_singleton.model : {vas_singleton.model_path}')

    return result, vas_singleton.model_path

def test_single():

    result, modelpath = classify_address(
        "45 spadina road"
    )

    print(f'result : {result}')


def match_entity(entity, entity_expected, entity_predicted):

    entity_expected = str(entity_expected)
    entity_predicted = str(entity_predicted)

    if(entity_predicted == '-'):
        entity_predicted = 'nan'

    if(
        (entity_expected != entity_predicted)
    ):
        print(f"failed to match {entity}:: [{entity_expected}] vs [{entity_predicted}]")
        return False
    
    return True

def is_match(expected, predicted):

    if(not match_entity('street_name', expected['street_name'], predicted['street_name'])):
        return False
    
    if(not match_entity('house_no', expected['house_no'], predicted['house_no'])):
        return False
    
    if(not match_entity('suite_no', expected['suite_no'], predicted['suite_no'])):
        return False

    return True

def hypenate(predicted, key):

    if(predicted[key] == 'null'):
        predicted[key] = '-'

    return predicted

def replace_null_with_hypen(predicted):

    for key, _ in predicted.items():
        predicted[key.lower()] = predicted.pop(key)

        predicted = hypenate(predicted, key.lower())

    # print(f'predicted: {predicted}')

    return predicted

def test_multiple():

    df = read_address_csv()

    # print(df)

    # return

    total_addresses = len(df)
    failed_addresses = 0
    no_address = 0
    for idx, row in df.iterrows():
        # if(row[COL_ADDRESS] != 'nan'):
        # print(f'{idx} row["address"] : {type(row["address"])}')
        # if(isinstance(type(row[COL_ADDRESS]), float)):
        #     continue
        c_address = row[COL_ADDRESS]
        expected_street_name = row['street_name']

        # print(f'c_address: {c_address}, c_address.type:{type(c_address)}')
        if(isinstance(c_address, float)):
            # print('skipping')
            no_address += 1
            continue

        if(expected_street_name == 'not_decided'):
            continue

        # Current (c_)
        expected_house_no = row['house_no']
        expected_suite_no = row['suite_no']

        

        # Current Predicted (c_)
        # cp_street_name = row['street_name.1']
        # cp_house_no = row['house_no.1']
        # cp_suite_no = row['suite_no.1']

        expected_dict = {
            'street_name'   : expected_street_name,
            'house_no'      : expected_house_no,
            'suite_no'      : expected_suite_no
        }

        
        # print(f'street_name: {type(c_street_name)}, house_no: {type(c_house_no)}, suite_no: {type(c_suite_no)}')
        # print(f'street_name: {c_street_name}, house_no: {c_house_no}, suite_no: {c_suite_no}')

        # print(f'{idx} c_address: {c_address}, street_name: {c_street_name}')

        predicted = vas_singleton.get_tokens(c_address)
        predicted = replace_null_with_hypen(predicted)
        # 

        match_result = is_match(expected_dict, predicted)

        if(match_result == False):
            print(f'\nc_address: {c_address}')
            print(f'\nExpected:\nstreet_name: {expected_street_name}\nhouse_no: {expected_house_no}\nsuite_no: {expected_suite_no}')
            print(f'\npredicted : {predicted}')

            print(f'match_result: {match_result}')

            print(f'\n' * 1)
        
            print(f'-' * 90)

            failed_addresses += 1
        else:
            # print(f'c_address: {c_address} successfully matched')
            # print(f'\n' * 1)

            # print(f'\nExpected:\nstreet_name: {expected_street_name}\nhouse_no: {expected_house_no}\nsuite_no: {expected_suite_no}')
            # print(f'\npredicted : {predicted}')

            # print(f'match_result: {match_result}')
        
            # print(f'-' * 90)

            pass

        # print(f'row : {row["address"]}')
        pass


    print(f'final:failed {failed_addresses} out of {total_addresses - no_address}')

def startpy():

    test_multiple()

    pass

if __name__ == '__main__':
    startpy()


'''
How to run?

py predict_local_2.py 

or

py predict_local_2.py /home/rajaraman/datasets/ecolab-ner-archive/ecolab_address_20240229_2.model.ser.gz

'''