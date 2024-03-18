
'''
Created on 

@author: Raja CSP Raman

source:
    ?
'''
import os
from dotenv import load_dotenv

load_dotenv()

# PORT_NO     = os.getenv("PORT_NO")
# APP_TITLE   = os.getenv("APP_TITLE")

PORT_NO     = 8262
APP_TITLE   = "Custom NER - Riversand"

ADDRESS_INPUT_BERT_CSV_PATH = os.getenv("ADDRESS_INPUT_BERT_CSV_PATH")
PATTERN_DEBUG               = True if (int(os.getenv("PATTERN_DEBUG")) == 1) else False

CORE_NLP_TRAINING_FILEPATH  = os.getenv("CORE_NLP_TRAINING_FILEPATH")
CORE_NLP_TESTING_FILEPATH   = os.getenv("CORE_NLP_TESTING_FILEPATH")
CORE_NLP_MODELNAME          = os.getenv("CORE_NLP_MODELNAME")

NER_MODEL_FOLDER_BASE       = os.getenv("NER_MODEL_FOLDER_BASE")

STREET_NAME                 = "STREET_NAME"
HOUSE_NO                    = "HOUSE_NO"
SUITE_NO                    = "SUITE_NO"
EMPTY                       = "0"

TESTING_FILEPATH            = os.getenv("TESTING_FILEPATH")

FINEL_NER_MODEL_BASE        = os.getenv("FINEL_NER_MODEL_BASE")



HEADERS = {
    'x-rdp-version': '8.1',
    "Content-Type": "application/json",
    'x-rdp-userId': 'system_user',
    'x-rdp-userRoles': '["admin"]',
    'x-rdp-clientId': 'match-feedbackClient',
    'x-rdp-appId': 'match-feedback'
}

# WEBURL      = "manage.rdpfsna20.riversand-dataplatform.com"
# TENANT_ID   = "ecolabuat"

WEBURL      = "manage.rdpenggqa1.riversand-dataplatform.com"
WEBPORT     = 8085
TENANT_ID = "cxshowcaseqa1"


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