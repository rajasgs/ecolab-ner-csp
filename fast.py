
'''
Created on 

@author: Raja CSP Raman

source:
    https://github.com/rajasgs/simple-fastapi/blob/main/main.py
'''

from fastapi.responses import (
    JSONResponse,
)

from pydantic import BaseModel

# import validator_single_extended as vase
import jpype

jpype.startJVM(classpath    = ['jars/*', "./"])

from fastapi import (
    # Depends,
    FastAPI,
    # Form,
    HTTPException,
    Query,
    Request,
    # Response,
    # status,
)

app = FastAPI(
    title       = "FastAPI",
    version     = "0.1.0",
    docs_url    = None,
    redoc_url   = None,
    openapi_url = None,
)

def get_tokens(address, core_nlp_modelname):

    model_path = f"{core_nlp_modelname}.model.ser.gz"

    simple_predict_class        = jpype.JClass("SimplePredictNERNoSingleton")

    result = simple_predict_class.getTokens(str(address), model_path)

    # print(result)

    result_parts = result.split('\n')

    street_name = result_parts[0].replace('STREET_NAME=', '')
    house_no    = result_parts[1].replace('HOUSE_NO=', '')
    suite_no    = result_parts[2].replace('SUITE_NO=', '')

    if(suite_no == 'null'):
        suite_no = 'null'

    token_dict = {
        "STREET_NAME"   : str(street_name),
        "HOUSE_NO"      : str(house_no),
        "SUITE_NO"      : str(suite_no),
    }

    return token_dict

def test_single(c_address, core_nlp_modelname):

    predicted = get_tokens(c_address, core_nlp_modelname)
    # print(predicted)

    return predicted

@app.get("/")
async def ping_api():

    total_results = {
        "one" : "two"
    }

    return JSONResponse(content=total_results)

@app.post("/predict")
async def api_predict_single(address: str, model_name: str):

    if("ecolab" not in model_name):
        model_name = f"ecolab_{model_name}"

    address_result = test_single(address, model_name)

    total_results = {
        "address" : address,
        "classified" : address_result
    }

    return JSONResponse(content=total_results)

class Item(BaseModel):
    address: str
    model_name: str
    
@app.post("/predict/json")
async def api_predict_json_single(item: Item):

    address = item.address
    model_name = item.model_name

    # if("ecolab" not in model_name):
    #     model_name = f"ecolab_{model_name}"

    address_result = test_single(address, model_name)

    total_results = {
        "address" : address,
        "classified" : address_result
    }

    return JSONResponse(content=total_results)


'''
uvicorn fast:app --reload

uvicorn fast:app --host "0.0.0.0" --port 8085 --workers 4

http://0.0.0.0:8000/

'''