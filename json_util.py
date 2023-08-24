
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

format:

entries : [
    {
        "address" : "254, Spadina Road",
        
        "street_name_original" : "Spadina Road"
        "house_no_original" : "254",
        "suite_no_original" :  "null",

        "street_name_predicted" : "Spadina Road",
        "house_no_predicted" : "254",
        "suite_no_predicted" : "null",

        "predicted_right" : "1"
    }
]
'''

import json
import faker_util as fu

JSON_FILEPATH = 'validator.json'

def create():
    try:
        file1 = open(JSON_FILEPATH,"x")
        data = json.dumps({
            "entries":[]
        })
        file1.close()

        file = open(JSON_FILEPATH,"w")
        file.write(data)
    except:
        return "json already exsists"

    return "json created"

def add():

    name, birth_place = fu.get_details_1()
    
    stud_dict = {
        "name"          : name,
        "birth_place"   : birth_place
    }

    file1 = open(JSON_FILEPATH,'r')
    data = json.load(file1)

    data['entries'].append(stud_dict)

    data1 = json.dumps(data)

    file1.close()

    file = open(JSON_FILEPATH,"w")
    file.write(data1)

    print("added")

def update_all(data):

    data1 = json.dumps(data)

    file = open(JSON_FILEPATH,"w")
    file.write(data1)

    print("added")

def update_single_address():

    file1 = open(JSON_FILEPATH,'r')
    data = json.load(file1)

    data['entries'].append()

    data1 = json.dumps(data)

    file1.close()

    file = open(JSON_FILEPATH,"w")
    file.write(data1)

    print("added")

def get_json_data():

    file1 = open(JSON_FILEPATH,'r')
    data = json.load(file1)

    return data

def add_address_base(
    address, 
    street_name, 
    house_no, 
    suite_no
):

    stud_dict = {
        "address" : address,
        
        "street_name_original" : street_name,
        "house_no_original" : house_no,
        "suite_no_original" :  suite_no,

        "street_name_predicted" : None,
        "house_no_predicted" : None,
        "suite_no_predicted" : None,

        "predicted_right" : None
    }

    file1 = open(JSON_FILEPATH,'r')
    data = json.load(file1)

    data['entries'].append(stud_dict)

    data1 = json.dumps(data)

    file1.close()

    file = open(JSON_FILEPATH,"w")
    file.write(data1)

    # print(f"added {address}")

def startpy():

    add()

if __name__ == '__main__':
    startpy()