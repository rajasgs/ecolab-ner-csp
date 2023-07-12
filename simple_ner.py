

'''
Created on 

@author: Raja CSP Raman

source:
    
'''

import subprocess

MODEL_NAME = 'eco1'
classpath = "jars/*"

def train_model():
    
    model_file        = f'{MODEL_NAME}.model.ser.gz'
    ner_prop_filename = f'{MODEL_NAME}.model.props'

    with open("one.txt", 'w') as f:
        result = subprocess.run(
            ['java',
                     '-Xmx1g',
                     '-cp', classpath,
                    'edu.stanford.nlp.ie.crf.CRFClassifier',
                    '-prop', ner_prop_filename], stdout = f
            )
    
    print("Done")
    return model_file


def startpy():
    train_model()

if __name__ == '__main__':
    startpy()