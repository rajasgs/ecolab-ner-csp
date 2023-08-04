import requests
import logging
import pprint
import json

headers = {
    'x-rdp-version': '8.1',
    "Content-Type": "application/json",
    'x-rdp-userId': 'system_user',
    'x-rdp-userRoles': '["admin"]',
    'x-rdp-clientId': 'match-feedbackClient',
    'x-rdp-appId': 'match-feedback'
}

WEBPORT = 8085
WEBURL = "manage.rdpfsna20.riversand-dataplatform.com"
TENANT_ID = "ecolabuat"

API_URL = f"http://{WEBURL}:{WEBPORT}/{TENANT_ID}/api/matchservice/standardize"


def prepare_payload(value):
    payload = {
        "entity": {
            "id": "test_standardize",
            "name": "test_standardize",
            "type": "customerSite",
            "data": {
                "attributes": {
                    "addressLine1Cleansed": {
                        "values": [
                            {
                                "id": "3_0_0",
                                "value": value,
                                "locale": "en-US",
                                "source": "internal"
                            }
                        ]
                    }
                }
            }
        }
    }
    
    return payload

def standardize_values(headers, list_of_addresses):
    session = requests.Session()
    session.headers.update(headers)
    standardized_addresses = []

    count = 1
    for address in list_of_addresses:
        payload = prepare_payload(address)
        response = session.post(API_URL, data=json.dumps(payload), timeout=60)        
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
    
    standardized_addresses = standardize_values(headers, values_list)

    write_object = open(filename+"_standardized.txt", "w")
    for value in standardized_addresses:
        write_object.writelines(value+"\n")
    write_object.close()

    logging.info(f"Dataset {filename} is standardized.")

if __name__ == "__main__":
    files = ["Ecolab_Address_Training_Ver2.txt", "Ecolab_Address_Testing_Ver2.txt"]
    for filename in files:
        standardize_dataset(filename)
