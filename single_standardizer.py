

import requests
import json

headers = {
    'x-rdp-version': '8.1',
    "Content-Type": "application/json",
    'x-rdp-userId': 'system_user',
    'x-rdp-userRoles': '["admin"]',
    'x-rdp-clientId': 'match-feedbackClient',
    'x-rdp-appId': 'match-feedback'
}
WEBPORT     = 8085
WEBURL      = "manage.rdpfsna20.riversand-dataplatform.com"
TENANT_ID   = "ecolabuat"

API_URL = f"http://{WEBURL}:{WEBPORT}/{TENANT_ID}/api/matchservice/standardize"

session = requests.Session()
session.headers.update(headers)

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

def standardize_single(address, count):

    payload = prepare_payload(address)
    response = session.post(API_URL, data=json.dumps(payload), timeout=60)        
    
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