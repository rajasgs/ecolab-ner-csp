

import jpype

class ValidatorSingletonExtended:
   
    __instance          = None
    singleton_predict   = None

    @staticmethod 
    def getInstance(model_path):
        """ Static access method. """
        if ValidatorSingletonExtended.__instance == None:
            ValidatorSingletonExtended(model_path)

        return ValidatorSingletonExtended.__instance
    
    def getFreshInstance(self):

        print('calling fresh init by reloading')

        print(f'self.model_path : {self.model_path}')

        simple_predict_class        = jpype.JClass("SimplePredictNER")
        self.singleton_predict      = simple_predict_class.getInstance(self.model_path)

        return ValidatorSingletonExtended.__instance
    
    def __init__(self, model_path):
        
        self.model_path          = model_path

        print('calling init')

        jpype.startJVM(classpath    = ['jars/*', "./"])
        simple_predict_class        = jpype.JClass("SimplePredictNER")
        self.singleton_predict      = simple_predict_class.getInstance(self.model_path)
        
        """ Virtually private constructor. """
        if ValidatorSingletonExtended.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ValidatorSingletonExtended.__instance = self


    def display (self):  
        print(f"[{self.model_path}]") 

    def get_tokens(self, address):

        result = self.singleton_predict.getTokens(str(address))

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
    
