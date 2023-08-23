'''
Created on 

@author: Raja CSP Raman

source:
    
'''


import jpype

MODEL_PATH = "Ecolab_address_ner_model_Ver1.model.ser.gz"

def get_tokens(singleton_predict, address):

    result = singleton_predict.getTokens(str(address))

    # print(result)

    result_parts = result.split('\n')

    street_name = result_parts[0].replace('STREET_NAME=', '')
    house_no    = result_parts[1].replace('HOUSE_NO=', '')
    suite_no    = result_parts[2].replace('SUITE_NO=', '')

    token_dict = {
        'STREET_NAME'   : street_name,
        'HOUSE_NO'      : house_no,
        'SUITE_NO'      : suite_no,
    }

    return token_dict

def singleton_test(filename):

    singleton_class = jpype.JClass("SingletonTest")

    singleton_instance = singleton_class.getInstance("two.txt")
    singleton_instance.printFilename()

def startpy():
    
    jpype.startJVM(classpath = ['jars/*', "./"])
    simple_predict_class = jpype.JClass("SimplePredictNER")
    singleton_predict = simple_predict_class.getInstance(MODEL_PATH)
    
    print(get_tokens(singleton_predict, "152 ST ANNE'S RD"))
    print(get_tokens(singleton_predict, "254 Spadina Road"))

    # print(singleton_test("one.txt"))

    # singleton_test("two.txt")

if __name__ == '__main__':
    startpy()