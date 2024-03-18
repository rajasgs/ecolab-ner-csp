
'''
Created on 

@author: Vishnu

source:
    Postman API:
    http://{{WEBURL}}:{{WEBPORT}}/{{TENANT_ID}}/api/matchservice/standardize
'''

import requests
import logging
import pprint
import json
import constants as cot


# Configure logging to print to the console with the specified format and level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def standardize_single_address(address):

    session = requests.Session()
    session.headers.update(cot.HEADERS)
    payload = cot.prepare_payload(address)

    response = session.post(cot.API_URL, data=json.dumps(payload), timeout=60)        
    if response.status_code != requests.codes.ok:
        logging.error(f"Error while standardizing value: {address}")
        exit()

    response = json.loads((response.content))
    # pprint.pprint(response)
    # print("Count: ",count)
    response = response["response"]
    if "status" not in response:
        return None
    
    if response["status"] == "success":
        standardized_value = response["entities"][0]["data"]["attributes"]["rssysmatch_addressLine1Cleansed"]["values"][0]["value"]
        # print(standardized_value)
        return standardized_value
    
    # if response["status"] == "error":
    logging.error(f"Error while standardizing value: {address}")
    # exit()
    return None

def standardize_values(headers, list_of_addresses):
    
    session = requests.Session()
    session.headers.update(headers)
    standardized_addresses = []

    count = 1
    for address in list_of_addresses:
        payload = cot.prepare_payload(address)
        response = session.post(cot.API_URL, data=json.dumps(payload), timeout=60)        
        if response.status_code != requests.codes.ok:
            logging.error(f"Error while standardizing record number: {count} value: {address}")
            exit()
        
        response = json.loads((response.content))
        # pprint.pprint(response)
        # print("Count: ",count)
        response = response["response"]
        if "status" in response:
            if response["status"] == "success":
                standardized_value = response["entities"][0]["data"]["attributes"]["rssysmatch_addressLine1Cleansed"]["values"][0]["value"]
                # print(standardized_value)
                standardized_addresses.append(standardized_value)
            
            if response["status"] == "error":
                logging.error(f"Error while standardizing record number: {count} value: {address}")
                exit()
        count += 1

    return standardized_addresses



def standardize_dataset(filename):
    read_object = open(filename, "r")
    values_list = read_object.readlines()
    read_object.close()
    logging.info(f"Number of records in {filename} : {len(values_list)}")
    
    standardized_addresses = standardize_values(cot.HEADERS, values_list)

    write_object = open(filename+"_standardized.txt", "w")
    for value in standardized_addresses:
        write_object.writelines(value+"\n")
    write_object.close()

    logging.info(f"Dataset {filename} is standardized.")

def startpy():

    # files = ["Ecolab_Address_Training_Ver2_1.txt", "Ecolab_Address_Testing_Ver2_1.txt"]

    files = [
        "z_address.txt", 
        # "march-06-testing.txt"
    ]
    
    for filename in files:
        standardize_dataset(filename)

    print(f"Done!")

if __name__ == "__main__":
    
    startpy()
