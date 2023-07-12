

'''
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/51588988/train-ner-model-in-stanford-nlp
'''

import subprocess

classpath = "jars/*"

model_file          = 'exp1.ser.gz'
ner_prop_filename   = 'custom-ner.prop'

def train_model():

    with open("ner_classification.txt", 'w') as f:
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


'''

java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier \
-prop propforclassifierone.prop
'''