

import requests
import json
import constants as cot


def standardize_single(address, count):

    session = requests.Session()
    session.headers.update(cot.HEADERS)
    payload = cot.prepare_payload(address)

    response = session.post(cot.API_URL, data=json.dumps(payload), timeout=60)        
    
    if response.status_code != requests.codes.ok:
        print(f"Error while standardizing record number: {count} value: {address}")
        exit()

    response = json.loads((response.content))
    # pprint.pprint(response)
    # print("Count: ",count)
    response = response["response"]
    if "status" in response:
        if response["status"] == "success":
            standardized_value = response["entities"][0]["data"]["attributes"]["rssysmatch_addressLine1Cleansed"]["values"][0]["value"]
            # print(standardized_value)
            return standardized_value
        
        if response["status"] == "error":
            print(f"Error while standardizing record number: {count} value: {address}")
        
    return None

def startpy():

    import sys
    
    addr = sys.argv[1]

    print(standardize_single(addr, 0))

    print(f"Done!")

if __name__ == "__main__":
    
    startpy()

'''
python single_standardizer.py "1173/38 u cementárny"
'''