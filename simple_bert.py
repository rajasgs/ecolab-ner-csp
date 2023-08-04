'''
Created on 

@author: Raja CSP Raman

source:
    
'''


from simpletransformers.ner import NERModel,NERArgs


model = NERModel('bert', 'outputs/', use_cuda=False)


def get_tokens(model, address):

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

def startpy():
    
    
    new_dict = get_tokens(model, "152 ST ANNE'S RD")

    print(new_dict)

    # print(singleton_test("one.txt"))

    # singleton_test("two.txt")

if __name__ == '__main__':
    startpy()