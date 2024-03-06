

'''

'''

import validator_single_extended as vase
import pandas as pd
from constants import *

FILEPATH = "~/datasets/Address-Pattern-NER-20240305-2.xlsx"

vas_singleton = vase.ValidatorSingletonExtended.getInstance(model_path = f"{CORE_NLP_MODELNAME}.model.ser.gz")

# MAX_READ_ROWS = 27

def is_unncessary_column(col_name):

    if("Unnamed:" in col_name):
        return True

    return False



def read_addess_full_excel():

    # Replace 'path_to_file.xlsx' with the path to your Excel file
    df = pd.read_excel(FILEPATH, sheet_name='base', engine='openpyxl', header = 1)

    return df

def read_addess_full_csv():

    df = df.read_csv("Address-Patterns-RS-address-ner-testing-20240229-1.csv", header=1)

    return df

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

def is_match(expected, predicted):

    if(
        (expected['street_name'] != predicted['street_name'])
    ):
        print(f"failed to match street_name: {expected['street_name']} : {predicted['street_name']}")
        return False
    
    if(
        (expected['house_no'] == predicted['house_no'])
    ):
        print(f"failed to match street_name: {expected['house_no']} : {predicted['house_no']}")
        return False
    
    if(
        (expected['suite_no'] == predicted['suite_no'])
    ):
        print(f"failed to match street_name: {expected['suite_no']} : {predicted['suite_no']}")
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
        # if(row['address'] != 'nan'):
        # print(f'{idx} row["address"] : {type(row["address"])}')
        # if(isinstance(type(row['address']), float)):
        #     continue
        c_address = row['address']
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

        # print(f'row : {row["address"]}')
        pass

    # for idx in range(5):
    #     result, modelpath = classify_address(
    #         "45 spadina road"
    #     )

    #     print(f'result : {result}')

    print(f'failed {failed_addresses} out of {total_addresses - no_address}')

def startpy():

    test_multiple()

    pass

if __name__ == '__main__':
    startpy()


'''
How to run?

Download 'address-ner-testing' from 
https://docs.google.com/spreadsheets/d/1RuTw-ycDOy2EUHf0qDp3kVvoZ0_s-bjd4eeRAyZndRk/edit#gid=806720616

as 
Address-Patterns-RS-address-ner-testing.csv


index,pattern index,address,street_name,house_no,suite_no,CoreNLP Output,street_name,house_no,suite_no,


'''