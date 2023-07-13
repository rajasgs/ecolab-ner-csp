

'''
Created on 

@author: Raja CSP Raman

source:
    
'''

import subprocess

classpath = "jars/*"

ner_prop_filename = f'exp6.model.props'

def train_model():
    
    model_file        = f'exp6.model.ser.gz'
    
    with open("exp6_output.txt", 'w') as f:
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