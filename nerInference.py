

'''
Created on 

@author: Raja CSP Raman

source:
    
    
'''



class NERInference:

    def __init__(self):

        pass

    def run_with_bert(self, dataframe):

        print('using BERT')

        dataframe[['STREET_NAME', 'HOUSE_NO', 'SUITE_NO']] = dataframe.apply(self.get_tokens_bert, axis = 1, result_type = 'expand')

        return dataframe