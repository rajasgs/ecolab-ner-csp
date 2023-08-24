
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


import pandas as pd

REVIEW_CSV_FILENAME = "validator.csv"


def append_original_to_csv(
    address,
    
    street_name_original    = None,
    house_no_original       = None,
    suite_no_original       = None 
):

    append_to_csv(
        address,
        
        street_name_original    = street_name_original,
        house_no_original       = house_no_original,
        suite_no_original       = suite_no_original,

        street_name_predicted   = None,
        house_no_predicted      = None,
        suite_no_predicted      = None,
        
        predicted_right         = None, 
    )

def append_to_csv(
    address,
    
    street_name_original    = None,
    house_no_original       = None,
    suite_no_original       = None,
    
    street_name_predicted   = None,
    house_no_predicted      = None,
    suite_no_predicted      = None,
    
    predicted_right         = None, 
):

    df = pd.read_csv(REVIEW_CSV_FILENAME)

    # append current review to the existing csv
    df2 = pd.DataFrame(
        [[
            address,
            street_name_original,
            house_no_original,
            suite_no_original,
            street_name_predicted,
            house_no_predicted,
            suite_no_predicted,
            predicted_right
        ]], 
        columns = [
            'address',
            'street_name_original',
            'house_no_original',
            'suite_no_original',
            'street_name_predicted',
            'house_no_predicted',
            'suite_no_predicted',
            'predicted_right'
        ]
    )
    df = pd.concat([df2, df])

    df = df.astype({
        "street_name_original" : str,
        "house_no_original" : int,
        "suite_no_original" : str,
    })

    df.to_csv(REVIEW_CSV_FILENAME, index = False)


def convert_data(content):

    if(not content):
        return content
    
    if(content == 'null'):
        return content
    
    return str((content))

def fill_predicted(
        c_index,

        street_name_predicted,
        house_no_predicted = None,
        suite_no_predicted = None,
        predicted_right = None,

        reason = None

    ):

    df = pd.read_csv(REVIEW_CSV_FILENAME)

    df.loc[c_index, 'street_name_predicted'] = street_name_predicted
    df.loc[c_index, 'suite_no_predicted'] = convert_data(suite_no_predicted)
    df.loc[c_index, 'house_no_predicted'] = convert_data(house_no_predicted)

    df.loc[c_index, 'predicted_right'] = predicted_right
    df.loc[c_index, 'reason'] = reason

    print(f'house_no_predicted : {house_no_predicted}')

    df = df.astype({
        "street_name_predicted" : str,
        "suite_no_predicted" : str,
        "house_no_predicted" : str,

        "predicted_right": str,
    })

    df.to_csv(REVIEW_CSV_FILENAME, index = False)

def get_df():

    df = pd.read_csv(REVIEW_CSV_FILENAME)

    return df

def get_row(c_index):

    df = pd.read_csv(REVIEW_CSV_FILENAME)

    row = df.iloc[c_index]

    return row