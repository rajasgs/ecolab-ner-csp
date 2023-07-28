'''
Created on 

@author: Raja CSP Raman

source:
    
'''


import jpype


def get_tokens(address):

    SampleClass = jpype.JClass("SimplePredictNER")

    result = SampleClass.getTokens(str(address))

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

def startpy():
    
    jpype.startJVM(classpath = ['jars/*', "./"])
    
    result = get_tokens("152 ST ANNE'S RD")
    print(result)

if __name__ == '__main__':
    startpy()