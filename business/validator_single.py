

import jpype

class ValidatorSingleton:
   
    __instance          = None
    singleton_predict   = None


    @staticmethod 
    def getInstance(model_version = "v1"):
        """ Static access method. """
        if ValidatorSingleton.__instance == None:
            ValidatorSingleton(model_version)

        if(ValidatorSingleton.__instance.model_version != model_version):
            ValidatorSingleton.__instance.reload_model(model_version) 

        return ValidatorSingleton.__instance
    
    def getFreshInstance(self):

        print('calling fresh init by reloading')

        print(f'self.model_version : {self.model_version}')
        print(f'self.model : {self.model}')

        simple_predict_class        = jpype.JClass("SimplePredictNER")
        self.singleton_predict      = simple_predict_class.getInstance(self.model)

        ValidatorSingleton.__instance = self

        return ValidatorSingleton.__instance
    
    def __init__(self, model_version):
        
        self.model_version  = model_version
        self.model          = f"models/{self.model_version}.model.ser.gz"

        print('calling init')

        jpype.startJVM(classpath    = ['jars/*', "./"])
        simple_predict_class        = jpype.JClass("SimplePredictNER")
        self.singleton_predict      = simple_predict_class.getInstance(self.model)
        
        """ Virtually private constructor. """
        if ValidatorSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ValidatorSingleton.__instance = self

    def reload_model(self, model_version):

        print(f'reloading model as the version changed to : {model_version}')

        self.model_version          = model_version
        self.model                  = f"models/{self.model_version}.model.ser.gz"

        simple_predict_class        = jpype.JClass("SimplePredictNER")
        self.singleton_predict      = simple_predict_class.getInstance(self.model)

        ValidatorSingleton.__instance = self.getFreshInstance()


    def display (self):  
        print("[%d, %s]"%(self.model_version, self.model)) 

    def get_tokens(self, address):

        result = self.singleton_predict.getTokens(str(address))

        # print(result)

        result_parts = result.split('\n')

        street_name = result_parts[0].replace('STREET_NAME=', '')
        house_no    = result_parts[1].replace('HOUSE_NO=', '')
        suite_no    = result_parts[2].replace('SUITE_NO=', '')

        if(suite_no == 'null'):
            suite_no = 'N/A'

        token_dict = {
            "STREET_NAME"   : str(street_name),
            "HOUSE_NO"      : str(house_no),
            "SUITE_NO"      : str(suite_no),
        }

        return token_dict