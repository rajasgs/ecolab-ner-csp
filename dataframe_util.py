
'''
Created on 

@author: Raja CSP Raman

source:


address,street_name_original,house_no_original,suite_no_original,street_name_predicted,house_no_predicted,suite_no_predicted,predicted_right
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

    df.to_csv(REVIEW_CSV_FILENAME, index = False)


def get_row(c_index):

    df = pd.read_csv(REVIEW_CSV_FILENAME)

    row = df.iloc[c_index]

    return row