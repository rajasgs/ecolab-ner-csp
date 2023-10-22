

from simpletransformers.ner import NERModel,NERArgs

model = None

local_dict = {
    "STREET_NAME" : "testing 1"
}

def set_dict(house_no):

    global local_dict

    local_dict['HOUSE_NO'] = house_no

def get_dict():

    return local_dict

def classify_address(
    address
):

    prediction, model_output = model.predict([address])
    
    # print(type(prediction[0]))

    new_dict = {
        'STREET_NAME' : '',
        'HOUSE_NO' : '',
        'SUITE_NO' : ''
    }
    for item in prediction[0]:
        # print(item)

        for c_index, c_item in item.items():
            # print(c_index, c_item)

            if(c_item in new_dict):

                if(len(new_dict[c_item].strip()) == 0):
                    new_dict[c_item] += c_index
                else:
                    new_dict[c_item] += ' ' + c_index

    return new_dict